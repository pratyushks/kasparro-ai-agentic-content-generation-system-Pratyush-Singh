from typing import Dict, Any, List
from ..models import Product, now_iso

class ComparisonPageAgent:
    """
    Builds a comparison page between two Product objects.
    Product B is fictional but follows same schema.
    """

    def build_comparison_page(self, primary: Product, secondary: Product) -> Dict[str, Any]:
        comparison_points: List[Dict[str, Any]] = [
            {
                "attribute": "Skin type",
                "primary_value": ", ".join(primary.skin_types),
                "secondary_value": ", ".join(secondary.skin_types),
            },
            {
                "attribute": "Vitamin C concentration",
                "primary_value": primary.vitamin_c_concentration,
                "secondary_value": secondary.vitamin_c_concentration,
            },
            {
                "attribute": "Key ingredients",
                "primary_value": ", ".join(primary.key_ingredients),
                "secondary_value": ", ".join(secondary.key_ingredients),
            },
            {
                "attribute": "Benefits",
                "primary_value": ", ".join(primary.benefits),
                "secondary_value": ", ".join(secondary.benefits),
            },
            {
                "attribute": "Price (INR)",
                "primary_value": primary.price_inr,
                "secondary_value": secondary.price_inr,
            },
        ]

        summary = (
            f"Both products are Vitamin C serums. {primary.name} is described as suitable for "
            f"{', '.join(primary.skin_types)} skin, while {secondary.name} in this fictional example "
            f"is described for {', '.join(secondary.skin_types)} skin."
        )

        page = {
            "page_type": "comparison",
            "primary_product": {
                "id": primary.id,
                "name": primary.name,
            },
            "secondary_product": {
                "id": secondary.id,
                "name": secondary.name,
            },
            "comparison_summary": {
                "headline": f"{primary.name} vs {secondary.name}",
                "summary": summary,
            },
            "comparison_points": comparison_points,
            "who_should_choose_which": {
                "primary_recommendation": (
                    f"Choose {primary.name} if you have {', '.join(primary.skin_types)} skin "
                    "and want a 10% Vitamin C serum that helps brighten skin and fade dark spots."
                ),
                "secondary_recommendation": (
                    f"Choose {secondary.name} if you have {', '.join(secondary.skin_types)} skin "
                    "and prefer this fictional alternative."
                ),
            },
            "generated_at": now_iso(),
        }
        return page
