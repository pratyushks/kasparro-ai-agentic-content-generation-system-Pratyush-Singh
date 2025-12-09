from dataclasses import dataclass, asdict
from typing import List, Literal, Dict, Any, Optional
from datetime import datetime

QuestionCategory = Literal["general", "usage", "safety", "benefits", "purchase", "comparison"]

@dataclass
class Product:
    id: str
    name: str
    vitamin_c_concentration: str
    skin_types: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price_inr: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            id=data["id"],
            name=data["name"],
            vitamin_c_concentration=data["vitamin_c_concentration"],
            skin_types=data["skin_types"],
            key_ingredients=data["key_ingredients"],
            benefits=data["benefits"],
            how_to_use=data["how_to_use"],
            side_effects=data["side_effects"],
            price_inr=int(data["price_inr"]),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Question:
    id: str
    category: QuestionCategory
    text: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FAQItem:
    id: str
    category: QuestionCategory
    question: str
    answer: str
    priority: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def now_iso() -> str:
    """Utility to standardize timestamps."""
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
