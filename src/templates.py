FAQ_PAGE_SCHEMA = """
faq_page:
{
  "page_type": "faq",
  "product": {"id": string, "name": string},
  "intro": string,
  "categories": [
    {
      "id": "general" | "usage" | "safety" | "benefits" | "purchase" | "comparison",
      "title": string,
      "faqs": [
        {
          "id": string,
          "category": same as parent category,
          "question": string,
          "answer": string,
          "priority": number between 0 and 1
        }
      ]
    },
    ...
  ],
  "generated_at": ISO-8601 timestamp string
}
"""

PRODUCT_PAGE_SCHEMA = """
product_page:
{
  "page_type": "product_detail",
  "product": {
    "id": string,
    "name": string,
    "price_inr": number
  },
  "hero_section": {
    "title": string,
    "tagline": string,
    "key_highlights": [string, ...]
  },
  "benefits_section": {
    "type": "benefits_block",
    "headline": string,
    "bullets": [string, ...]
  },
  "usage_section": {
    "type": "usage_block",
    "headline": string,
    "steps": [string, ...],
    "frequency_note": string
  },
  "ingredients_section": {
    "headline": "Key ingredients",
    "list": [string, ...]
  },
  "safety_section": {
    "type": "safety_block",
    "headline": string,
    "notes": [string, ...],
    "sensitive_skin_warning": string
  },
  "price_section": {
    "type": "price_block",
    "headline": "Price",
    "currency": "INR",
    "amount": number,
    "note": string
  },
  "faq_preview_section": {
    "headline": "Top questions",
    "faqs": [ FAQ item objects ... ]
  },
  "generated_at": ISO-8601 timestamp string
}
"""

COMPARISON_PAGE_SCHEMA = """
comparison_page:
{
  "page_type": "comparison",
  "primary_product": {
    "id": string,
    "name": string
  },
  "secondary_product": {
    "id": string,
    "name": string
  },
  "comparison_summary": {
    "headline": string,
    "summary": string
  },
  "comparison_points": [
    {
      "attribute": string,
      "primary_value": string | number,
      "secondary_value": string | number
    },
    ...
  ],
  "who_should_choose_which": {
    "primary_recommendation": string,
    "secondary_recommendation": string
  },
  "generated_at": ISO-8601 timestamp string
}
"""

# FULL_OUTPUT_SCHEMA = f"""
# Overall output JSON must be:

# {{
#   "faq_page": {FAQ_PAGE_SCHEMA},
#   "product_page": {PRODUCT_PAGE_SCHEMA},
#   "comparison_page": {COMPARISON_PAGE_SCHEMA}
# }}

# You must return EXACTLY this JSON structure, with no extra top-level fields.
# """
