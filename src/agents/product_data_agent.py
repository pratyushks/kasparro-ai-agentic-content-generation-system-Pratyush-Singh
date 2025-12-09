import json
from pathlib import Path
from typing import Dict
from ..models import Product

class ProductDataAgent:
    """
    Reads product JSON files and converts them to Product models.
    Single responsibility: parsing and basic validation.
    """

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)

    def load_products(self) -> Dict[str, Product]:
        glowboost_path = self.data_dir / "glowboost.json"
        product_b_path = self.data_dir / "product_b.json"

        products = {}
        for path in [glowboost_path, product_b_path]:
            with path.open("r", encoding="utf-8") as f:
                raw = json.load(f)
            product = Product.from_dict(raw)
            products[product.id] = product

        return products
