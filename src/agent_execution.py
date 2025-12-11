import json
from pathlib import Path
from src.agents.question_agent import run_question_agent
from src.agents.faq_agent import run_faq_agent
from src.agents.page_agent import run_page_agent

OUTPUT_DIR = Path("output")

def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    ensure_output_dir()

    # 1. Generate questions
    print("Running QuestionGeneratorAgent...")
    questions_json = run_question_agent()
    (OUTPUT_DIR / "questions.json").write_text(
        json.dumps(questions_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 2. Generate FAQs
    print("Running FAQAgent...")
    faq_items_json = run_faq_agent(questions_json)
    (OUTPUT_DIR / "faq_items.json").write_text(
        json.dumps(faq_items_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 3. Build pages (FAQ + product + comparison)
    print("Running PageAssemblyAgent...")
    pages_json = run_page_agent(faq_items_json)

    faq_page = pages_json["faq_page"]
    product_page = pages_json["product_page"]
    comparison_page = pages_json["comparison_page"]

    (OUTPUT_DIR / "faq.json").write_text(
        json.dumps(faq_page, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUTPUT_DIR / "product_page.json").write_text(
        json.dumps(product_page, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUTPUT_DIR / "comparison_page.json").write_text(
        json.dumps(comparison_page, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Completed. Output Generated:")
    print("   - output/questions.json")
    print("   - output/faq_items.json")
    print("   - output/faq.json")
    print("   - output/product_page.json")
    print("   - output/comparison_page.json")


if __name__ == "__main__":
    main()