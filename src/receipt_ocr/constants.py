_DEFAULT_OPENAI_MODEL = "gpt-4.1"

DEFAULT_RECEIPT_SCHEMA = {
    "merchant_name": "string",
    "merchant_address": "string",
    "transaction_date": "string",
    "transaction_time": "string",
    "total_amount": "number",
    "payment_method": "string",
    "payment_data": {
        "card_brand": "string",
        "card_last4": "string",
        "reference": "string",
        "authorization_code": "string",
    },
    "line_items": [
        {
            "item_name": "string",
            "item_quantity": "number",
            "item_price": "number",
        }
    ],
}
