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


def _build_question_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are the QuestionGeneratorAgent.\n"
                    "Your goal is to generate at least 15 UNIQUE user questions "
                    "about the primary product (GlowBoost Vitamin C Serum), using "
                    "ONLY the JSON product data obtained via tools.\n\n"
                    "You MUST first conceptually access the product JSON (it will be provided "
                    "to you in the prompt).\n\n"
                    "Do not invent new product-specific facts beyond what is in the dataset. "
                    "You may ask generic questions (e.g. about price, safety, usage), "
                    "but they must be consistent with the fields provided.\n\n"
                    "Valid categories for questions: "
                    "\"general\", \"usage\", \"safety\", \"benefits\", \"purchase\", \"comparison\".\n\n"
                    "Your final answer MUST be STRICT JSON with this exact shape:\n"
                    "{{\n"
                    "  \"questions\": [\n"
                    "    {{\"id\": \"q1\", \"category\": \"usage\", \"text\": \"...\"}},\n"
                    "    {{\"id\": \"q2\", \"category\": \"safety\", \"text\": \"...\"}},\n"
                    "    ... at least 15 items ...\n"
                    "  ]\n"
                    "}}\n"
                ),
            ),
            (
                "human",
                "Here is the product JSON:\n\n{product_json}\n\n"
                "Generate the questions now."
            ),
        ]
    )


def run_question_agent() -> Dict[str, Any]:
    product_json = get_product_data.invoke("primary")

    llm = _get_gemini_llm(temperature=0.3)

    prompt = _build_question_prompt()
    messages = prompt.invoke({"product_json": product_json})

    response = llm.invoke(messages.to_messages())

    if isinstance(response.content, str):
        output_str = response.content
    else:
        output_str = "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in (response.content or [])
        )

    return extract_json_object(output_str)