import yaml
from copy import deepcopy
from datetime import date
from recurring_cost_tracker import ExpenseAccount, Expense

YAML_CONTENT = {
    "name": "General",
    "currency": "EUR",
    "rebalance_interval": "monthly",
    "expenses": [
        {
            "name": "Bank Account",
            "category": "Essential",
            "payment": {
                "amount": 25,
                "currency": "EUR",
                "interval": 1,
                "interval_unit": "year",
                "next_payment_date": date(2024, 1, 1),
            },
        },
        {
            "name": "Barbier",
            "category": "Essential",
            "payment": {
                "amount": 30,
                "currency": "EUR",
                "interval": 6,
                "interval_unit": "week",
                "next_payment_date": date(2023, 10, 12),
            },
        },
    ],
}
