import json
from copy import deepcopy
from typing import Any

def build_default_categorization_guidance() -> str:
    """Build prompt instructions for free-form taxonomy output."""
    return """
If the output schema contains a `taxonomy` object:
- Always populate `taxonomy.category` and `taxonomy.subcategory` with the best free-form labels for the overall receipt.
- If no category taxonomy list was supplied by the caller, leave `taxonomy.category_id`, `taxonomy.category_name`, `taxonomy.subcategory_id`, and `taxonomy.subcategory_name` as empty strings.
"""


def build_categorization_guidance(categories: list[dict[str, Any]] | None) -> str:
    """Build prompt instructions for receipt-level categorization."""
    if not categories:
        return ""

    categories_json = json.dumps(categories, indent=2)
    return f"""
The caller supplied a category taxonomy for receipt-level classification.

Across all line items together:
- Always populate `taxonomy.category` and `taxonomy.subcategory` with the best free-form labels for the overall receipt purchase.
- Choose the single best matching category and subcategory using the provided ids, names, and descriptions.
- Populate `taxonomy.category_id`, `taxonomy.category_name`, `taxonomy.subcategory_id`, and `taxonomy.subcategory_name` using only values from this taxonomy.
- Do not assign taxonomy fields per line item. These fields belong inside the top-level `taxonomy` object of the receipt output.
- If no confident taxonomy category matches, still populate `taxonomy.category` and `taxonomy.subcategory` with your best free-form labels and return empty strings for the taxonomy-mapped fields.
- If a taxonomy category matches but no subcategory matches, populate the taxonomy category fields and leave the taxonomy subcategory fields empty.

Allowed category taxonomy:

```json
{categories_json}
```
"""
