import json
from typing import Any, Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from src.tools import get_product_data
from src.config import GOOGLE_API_KEY
from src.json_utils import extract_json_object

def _get_gemini_llm(temperature: float = 0.2) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=temperature,
        google_api_key=GOOGLE_API_KEY,
    )


def _build_page_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are the PageAssemblyAgent.\n"
                    "You will build three fully structured JSON pages:\n"
                    "- faq_page\n"
                    "- product_page\n"
                    "- comparison_page\n\n"
                    "You MUST use ONLY the fields from the provided product JSONs "
                    "for product-specific claims, and the provided FAQ items for FAQ content.\n\n"
                    "The primary product JSON and comparison product JSON will be provided. "
                    "The FAQ items JSON will also be provided.\n\n"
                    "Your final answer MUST be a single JSON object with exactly these top-level keys:\n"
                    "{{\n"
                    "  \"faq_page\": {{...}},\n"
                    "  \"product_page\": {{...}},\n"
                    "  \"comparison_page\": {{...}}\n"
                    "}}\n\n"
                    "Each page must itself be a valid JSON object. Do NOT wrap the JSON in backticks."
                ),
            ),
            (
                "human",
                "Here is the primary product JSON:\n\n{primary_product_json}\n\n"
                "Here is the comparison product JSON:\n\n{comparison_product_json}\n\n"
                "Here are the FAQ items from the previous step:\n\n{faq_items_json}\n\n"
                "Build the three pages now."
            ),
        ]
    )


def run_page_agent(faq_items_json: Dict[str, Any]) -> Dict[str, Any]:
    primary_json = get_product_data.invoke("primary")
    comparison_json = get_product_data.invoke("comparison")

    llm = _get_gemini_llm(temperature=0.2)
    prompt = _build_page_prompt()

    messages = prompt.invoke(
        {
            "primary_product_json": primary_json,
            "comparison_product_json": comparison_json,
            "faq_items_json": json.dumps(faq_items_json, ensure_ascii=False),
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