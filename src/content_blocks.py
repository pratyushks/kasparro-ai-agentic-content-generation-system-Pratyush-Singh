from typing import Dict, Any, List
from .models import Product

def build_overview_block(product: Product) -> Dict[str, Any]:
    skin_types = ", ".join(product.skin_types)
    return {
        "type": "overview_block",
        "title": product.name,
        "subtitle": f"{product.vitamin_c_concentration} Vitamin C serum for {skin_types} skin.",
        "summary": (
            "This serum is described as helping with brightening and fading the appearance of dark spots."
        )
    }


def build_benefits_block(product: Product) -> Dict[str, Any]:
    bullets: List[str] = []
    if "Brightening" in product.benefits:
        bullets.append("Helps brighten the look of your skin.")
    if "Fades dark spots" in product.benefits:
        bullets.append("Helps fade the appearance of dark spots over time.")
    if not bullets:
        bullets = [b for b in product.benefits]

    return {
        "type": "benefits_block",
        "headline": "Benefits",
        "bullets": bullets
    }


def build_usage_block(product: Product) -> Dict[str, Any]:
    return {
        "type": "usage_block",
        "headline": "How to use",
        "steps": [
            "Start with clean, dry skin.",
            product.how_to_use,
        ],
        "frequency_note": "Use once daily in the morning."
    }


def build_safety_block(product: Product) -> Dict[str, Any]:
    notes: List[str] = []
    if "tingling" in product.side_effects.lower():
        notes.append("May cause mild tingling for sensitive skin.")
    else:
        notes.append(product.side_effects)

    return {
        "type": "safety_block",
        "headline": "Safety & side effects",
        "notes": notes,
        "sensitive_skin_warning": "Patch test first if your skin tends to be sensitive."
    }


def build_price_block(product: Product) -> Dict[str, Any]:
    return {
        "type": "price_block",
        "headline": "Price",
        "currency": "INR",
        "amount": product.price_inr,
        "note": f"Listed price: ₹{product.price_inr}."
    }
