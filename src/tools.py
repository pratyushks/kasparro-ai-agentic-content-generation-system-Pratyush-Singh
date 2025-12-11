from pathlib import Path
import json
from typing import Literal
from langchain_core.tools import tool

DATA_DIR = Path("data")

@tool("get_product_data")
def get_product_data(kind: Literal["primary", "comparison"]) -> str:
    """
    Return the structured JSON data for a product as a JSON string.
    kind = "primary"    -> GlowBoost from glowboost.json
    kind = "comparison" -> Product B from product_b.json
    """
    if kind == "primary":
        path = DATA_DIR / "glowboost.json"
    elif kind == "comparison":
        path = DATA_DIR / "product_b.json"
    else:
        raise ValueError("kind must be 'primary' or 'comparison'")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return json.dumps(data, ensure_ascii=False)
