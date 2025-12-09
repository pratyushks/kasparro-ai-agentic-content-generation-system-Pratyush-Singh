from typing import Dict, Any, List
from ..models import Product, FAQItem, now_iso, QuestionCategory

class FAQPageAgent:
    """
    Builds the FAQ page JSON from FAQ items.
    """

    CATEGORY_META = {
        "general": "General",
        "usage": "How to use",
        "safety": "Safety & side effects",
        "benefits": "Benefits",
        "purchase": "Price & purchase",
        "comparison": "Comparisons",
    }

    def build_faq_page(self, product: Product, faq_items: List[FAQItem]) -> Dict[str, Any]:
        categories: Dict[QuestionCategory, Dict[str, Any]] = {}
        for cat_id, title in self.CATEGORY_META.items():
            categories[cat_id] = {
                "id": cat_id,
                "title": title,
                "faqs": [],
            }

        for faq in faq_items:
            cat = faq.category
            categories[cat]["faqs"].append(faq.to_dict())

        page = {
            "page_type": "faq",
            "product": {
                "id": product.id,
                "name": product.name,
            },
            "intro": f"Find answers to common questions about {product.name}.",
            "categories": list(categories.values()),
            "generated_at": now_iso(),
        }
        return page
