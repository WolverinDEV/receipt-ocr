from receipt_ocr.categorization import (
    build_categorization_guidance,
    build_default_categorization_guidance,
)

def test_build_default_categorization_guidance():
    guidance = build_default_categorization_guidance()

    assert "`taxonomy` object" in guidance
    assert "`taxonomy.category`" in guidance
    assert "`taxonomy.category_id`" in guidance


def test_build_categorization_guidance():
    categories = [
        {
            "id": "groceries",
            "description": "Food and household goods",
            "subcategories": [
                {"id": "oral-care", "description": "Toothpaste and brushes"}
            ],
        }
    ]

    guidance = build_categorization_guidance(categories)

    assert "groceries" in guidance
    assert "oral-care" in guidance
    assert "Across all line items together" in guidance
    assert "top-level `taxonomy` object" in guidance
    assert "taxonomy.category_id" in guidance
