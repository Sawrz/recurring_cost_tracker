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


def test_from_yaml(monkeypatch, tmp_path):
    def mock_expense():
        return Expense("Name", "Category", 13.37, "EUR", 2, "week", date(1970, 1, 1))

    monkeypatch.setattr(yaml, "load", lambda *args, **kwargs: deepcopy(YAML_CONTENT))
    monkeypatch.setattr(Expense, "from_dict", lambda *args, **kwargs: mock_expense)

    file_path = tmp_path / "test_file.yaml"
    file_path.write_text("")

    account = ExpenseAccount.from_yaml(file_path)

    assert account.name == YAML_CONTENT["name"]
    assert account.currency == YAML_CONTENT["currency"]
    assert account.rebalance_interval == YAML_CONTENT["rebalance_interval"]
    assert len(account.expenses) == 2
