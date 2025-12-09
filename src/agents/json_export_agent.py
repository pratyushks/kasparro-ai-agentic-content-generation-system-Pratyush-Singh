import json
from pathlib import Path
from typing import Dict, Any

class JsonExportAgent:
    """
    Validates and writes JSON pages.
    """

    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_pages(
        self,
        faq_page: Dict[str, Any],
        product_page: Dict[str, Any],
        comparison_page: Dict[str, Any],
    ) -> None:
        self._write_json("faq.json", faq_page)
        self._write_json("product_page.json", product_page)
        self._write_json("comparison_page.json", comparison_page)

    def _write_json(self, filename: str, data: Dict[str, Any]) -> None:
        path = self.output_dir / filename
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
