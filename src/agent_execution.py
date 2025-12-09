from pathlib import Path
from .agents.product_data_agent import ProductDataAgent
from .agents.question_generator_agent import QuestionGeneratorAgent
from .agents.faq_agent import FAQAgent
from .agents.content_block_agent import ContentBlockAgent
from .agents.product_page_agent import ProductPageAgent
from .agents.faq_page_agent import FAQPageAgent
from .agents.comparison_page_agent import ComparisonPageAgent
from .agents.json_export_agent import JsonExportAgent

def run_pipeline() -> None:
    # 1. Load products
    data_agent = ProductDataAgent(data_dir=str(Path("data")))
    products = data_agent.load_products()

    glowboost = products["glowboost-vitamin-c-serum"]
    product_b = next(p for pid, p in products.items() if pid != glowboost.id)

    # 2. Generate questions
    q_agent = QuestionGeneratorAgent()
    questions = q_agent.generate_questions(glowboost)

    # 3. Generate FAQs
    faq_agent = FAQAgent()
    faq_items = faq_agent.generate_faq_items(glowboost, questions)

    # 4. Build content blocks
    cb_agent = ContentBlockAgent()
    blocks = cb_agent.build_blocks(glowboost)

    # 5. Build product page
    product_page_agent = ProductPageAgent()
    product_page = product_page_agent.build_product_page(glowboost, blocks, faq_items)

    # 6. Build FAQ page
    faq_page_agent = FAQPageAgent()
    faq_page = faq_page_agent.build_faq_page(glowboost, faq_items)

    # 7. Build comparison page
    comparison_agent = ComparisonPageAgent()
    comparison_page = comparison_agent.build_comparison_page(glowboost, product_b)

    # 8. Export all pages as JSON
    exporter = JsonExportAgent(output_dir="output")
    exporter.export_pages(faq_page, product_page, comparison_page)

    print("Generated pages in ./output: faq.json, product_page.json, comparison_page.json")


if __name__ == "__main__":
    run_pipeline()
