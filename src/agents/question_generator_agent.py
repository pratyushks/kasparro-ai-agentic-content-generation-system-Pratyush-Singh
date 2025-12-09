from typing import List
from ..models import Product, Question

class QuestionGeneratorAgent:
    """
    Generates at least 15 user questions for a given product.
    Only uses structured product data.
    """

    def generate_questions(self, product: Product) -> List[Question]:
        name = product.name

        questions: List[Question] = [
            # general
            Question("q1", "general", f"What does {name} do?"),
            Question("q2", "general", f"Who is {name} suitable for?"),

            # usage
            Question("q3", "usage", f"How should I apply {name}?"),
            Question("q4", "usage", f"How often can I use {name}?"),
            Question("q5", "usage", f"Should I use {name} in the morning or at night?"),
            Question("q6", "usage", f"Can I use {name} with other skincare products?"),

            # safety
            Question("q7", "safety", f"Is {name} safe for sensitive skin?"),
            Question("q8", "safety", f"What side effects can I expect from {name}?"),
            Question("q9", "safety", f"What should I do if I feel irritation after using {name}?"),

            # benefits
            Question("q10", "benefits", f"Will {name} brighten my skin?"),
            Question("q11", "benefits", f"Can {name} help fade dark spots?"),

            # purchase
            Question("q12", "purchase", f"What is the price of {name}?"),
            Question("q13", "purchase", f"Is {name} good value for its price?"),

            # comparison
            Question("q14", "comparison", f"How is {name} different from other Vitamin C serums?"),
            Question("q15", "comparison", f"Is {name} suitable if I already use another Vitamin C product?"),
        ]

        return questions