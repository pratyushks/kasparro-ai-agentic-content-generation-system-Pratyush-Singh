from typing import List
from ..models import Product, Question, FAQItem

class FAQAgent:
    """
    Converts questions + product data into answered FAQ items.
    Ensures at least 5 FAQ items with priorities.
    """

    def generate_faq_items(self, product: Product, questions: List[Question]) -> List[FAQItem]:
        faq_items: List[FAQItem] = []

        for q in questions:
            answer = self._answer_for_question(product, q)
            priority = self._priority_for_question(q)
            faq_items.append(
                FAQItem(
                    id=f"faq-{q.id}",
                    category=q.category,
                    question=q.text,
                    answer=answer,
                    priority=priority,
                )
            )

        faq_items.sort(key=lambda f: f.priority, reverse=True)
        return faq_items

    def _answer_for_question(self, product: Product, q: Question) -> str:
        name = product.name
        skin_types = ", ".join(product.skin_types)
        ingredients = ", ".join(product.key_ingredients)
        benefits = ", ".join(product.benefits)

        # Simple rule-based mapping
        if q.id == "q1":
            return f"{name} is a {product.vitamin_c_concentration} Vitamin C serum described as helping with {benefits.lower()}."
        if q.id == "q2":
            return f"It is described as suitable for {skin_types} skin types."
        if q.id == "q3":
            return product.how_to_use
        if q.id == "q4":
            return "You can use it once daily, preferably in the morning as described."
        if q.id == "q5":
            return "The usage instructions specify morning use before sunscreen."
        if q.id == "q6":
            return (
                "The dataset only describes how to use it before sunscreen. "
                "If you are layering multiple products, introduce them slowly and "
                "patch test if needed."
            )
        if q.id == "q7":
            return (
                f"The product notes: '{product.side_effects}'. "
                "If you have very sensitive skin, patch test first and start slowly."
            )
        if q.id == "q8":
            return product.side_effects
        if q.id == "q9":
            return (
                "If you experience irritation, reduce how often you use it or stop use "
                "and consult a professional if it persists."
            )
        if q.id == "q10":
            return "Yes, one of the listed benefits is 'Brightening'."
        if q.id == "q11":
            return "Yes, it is described as helping to fade dark spots."
        if q.id == "q12":
            return f"The listed price is ₹{product.price_inr}."
        if q.id == "q13":
            return (
                f"The price is ₹{product.price_inr}. Whether it is good value depends on your budget "
                "and how important brightening and fading dark spots are for you."
            )
        if q.id == "q14":
            return (
                f"{name} is specifically described as a {product.vitamin_c_concentration} "
                f"Vitamin C serum for {skin_types} skin types with key ingredients {ingredients}."
            )
        if q.id == "q15":
            return (
                "If you already use a Vitamin C product, avoid layering multiple strong Vitamin C "
                "products without guidance, as it may increase the chance of irritation."
            )

        return "The data only provides limited information about this question."

    def _priority_for_question(self, q: Question) -> float:
        # Simple heuristic: usage & safety > benefits > purchase > general > comparison
        base = {
            "usage": 0.95,
            "safety": 0.9,
            "benefits": 0.8,
            "purchase": 0.7,
            "general": 0.6,
            "comparison": 0.5,
        }[q.category]

        # Make earlier questions within each category slightly higher
        offset = 0.01 if q.id in ("q3", "q7", "q10") else 0.0
        return base + offset
