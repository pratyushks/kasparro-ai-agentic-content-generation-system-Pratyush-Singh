from typing import Dict, Any
from ..models import Product
from ..content_blocks import (
    build_overview_block,
    build_benefits_block,
    build_usage_block,
    build_safety_block,
    build_price_block,
)

class ContentBlockAgent:
    """
    Wraps the content logic block functions into a single agent.
    """

    def build_blocks(self, product: Product) -> Dict[str, Any]:
        return {
            "overview_block": build_overview_block(product),
            "benefits_block": build_benefits_block(product),
            "usage_block": build_usage_block(product),
            "safety_block": build_safety_block(product),
            "price_block": build_price_block(product),
        }
