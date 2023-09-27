import yaml
import pandas as pd
from sqlite3 import connect
from pathlib import Path
from .expenses import Expense


class ExpenseAccount:
    def __init__(self, name: str, expenses: list, currency: str, rebalance_interval: str) -> None:
        self.name = name
        self.expenses = expenses
        self.currency = currency
        self.rebalance_interval = rebalance_interval

    @classmethod
    def from_yaml(cls, file_path: Path, log_level: str = "WARNING"):
        with open(file_path, "r") as content:
            account_config = yaml.load(content, Loader=yaml.SafeLoader)

        expenses = [Expense.from_dict(exp) for exp in account_config["expenses"]]

        return cls(account_config["name"], expenses, account_config["currency"], account_config["rebalance_interval"])





