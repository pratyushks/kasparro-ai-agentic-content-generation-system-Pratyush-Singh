from typing import Dict, Any, List
from ..models import Product, FAQItem, now_iso

class ProductPageAgent:
    """
    Assembles the product detail page JSON from product + content blocks + FAQs.
    """

    def build_product_page(
        self,
        product: Product,
        content_blocks: Dict[str, Any],
        faq_items: List[FAQItem],
    ) -> Dict[str, Any]:
        top_faqs = [faq.to_dict() for faq in faq_items[:3]]

        skin_types = ", ".join(product.skin_types)
        hero = {
            "title": product.name,
            "tagline": f"{product.vitamin_c_concentration} Vitamin C serum for {skin_types} skin.",
            "key_highlights": [
                f"Suitable for {skin_types} skin types.",
                "Helps brighten skin and fade dark spots.",
            ],
        }

        page: Dict[str, Any] = {
            "page_type": "product_detail",
            "product": {
                "id": product.id,
                "name": product.name,
                "price_inr": product.price_inr,
            },
            "hero_section": hero,
            "benefits_section": content_blocks["benefits_block"],
            "usage_section": content_blocks["usage_block"],
            "ingredients_section": {
                "headline": "Key ingredients",
                "list": product.key_ingredients,
            },
            "safety_section": content_blocks["safety_block"],
            "price_section": content_blocks["price_block"],
            "faq_preview_section": {
                "headline": "Top questions",
                "faqs": top_faqs,
            },
            "generated_at": now_iso(),
        }
        return page
