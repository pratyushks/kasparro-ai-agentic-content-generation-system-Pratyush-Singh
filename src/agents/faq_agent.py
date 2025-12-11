import json
from typing import Any, Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from src.tools import get_product_data
from src.config import GOOGLE_API_KEY
from src.json_utils import extract_json_object

def _get_gemini_llm(temperature: float = 0.3) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=temperature,
        google_api_key=GOOGLE_API_KEY,
    )


def _build_faq_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are the FAQAgent.\n"
                    "You receive a list of user questions for the primary product.\n"
                    "You must answer each question using ONLY information from the product JSON, "
                    "plus generic safety/usage advice that does not add new product-specific claims.\n\n"
                    "For example, you may say 'patch test if you have sensitive skin', "
                    "but you must not invent efficacy claims like 'works in 2 weeks'.\n\n"
                    "The product JSON will be provided to you.\n\n"
                    "Input questions JSON shape:\n"
                    "{{\n"
                    "  \"questions\": [ {{\"id\": \"q1\", \"category\": \"...\", \"text\": \"...\"}}, ... ]\n"
                    "}}\n\n"
                    "Your final answer MUST be STRICT JSON of shape:\n"
                    "{{\n"
                    "  \"faq_items\": [\n"
                    "    {{\n"
                    "      \"id\": \"faq-q1\",\n"
                    "      \"category\": \"usage\",\n"
                    "      \"question\": \"...\",\n"
                    "      \"answer\": \"...\",\n"
                    "      \"priority\": 0.95\n"
                    "    }},\n"
                    "    ... one for each input question ...\n"
                    "  ]\n"
                    "}}\n"
                    "Priorities are numbers between 0 and 1 (higher = more important)."
                ),
            ),
            (
                "human",
                "Here is the product JSON:\n\n{product_json}\n\n"
                "Here is the questions JSON:\n\n{questions_json}\n\n"
                "Generate FAQ items now."
            ),
        ]
    )


def run_faq_agent(questions_json: Dict[str, Any]) -> Dict[str, Any]:
    product_json = get_product_data.invoke("primary")

    llm = _get_gemini_llm(temperature=0.3)
    prompt = _build_faq_prompt()

    messages = prompt.invoke(
        {
            "product_json": product_json,
            "questions_json": json.dumps(questions_json, ensure_ascii=False),
        }
    )

    response = llm.invoke(messages.to_messages())

    if isinstance(response.content, str):
        output_str = response.content
    else:
        output_str = "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in (response.content or [])
        )

    return extract_json_object(output_str)