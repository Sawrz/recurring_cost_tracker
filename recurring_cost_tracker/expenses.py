from .exceptions import FileTypeException
from datetime import date
from dateutil.relativedelta import relativedelta

class Expense:
    def __init__(
        self,
        name: str,
        category: str,
        amount: float,
        currency: str,
        payment_interval: int,
        payment_interval_unit: str,
        next_payment_date: date,
    ) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.currency = currency
        self.payment_delta = self._infer_timedelta(payment_interval, payment_interval_unit)
        self.next_payment_date = next_payment_date

    @classmethod
    def from_dict(cls, exp_dict):
        exp_dict.update(exp_dict["payment_dict"])
        del exp_dict["payment"]

        return cls(**exp_dict)

    @staticmethod
    def _infer_timedelta(payment_interval: int, payment_interval_unit: str):
        if payment_interval_unit == "week":
            return relativedelta(weeks=payment_interval)
        elif payment_interval_unit == "month":
            return relativedelta(months=payment_interval)
        elif payment_interval == "year":
            return relativedelta(years=payment_interval)

    @staticmethod
    def _type_check(value, exp_type):
        if not isinstance(value, exp_type):
            raise FileTypeException(
                f"Wrong file type provided for {value}. {type(value)} was provided but expected {exp_type}"
            )

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._type_check(value, str)
        self.name = value

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self, value):
        self._type_check(value, str)
        self.category = value

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, value):
        self._type_check(value, float)
        self.amount = value

    @property
    def currency(self):
        return self.amount

    @currency.setter
    def currency(self, value):
        self._type_check(value, str)
        self.currency = value

    @property
    def payment_delta(self):
        return self.payment_delta

    @payment_delta.setter
    def payment_delta(self, value):
        self._type_check(value, relativedelta)
        self.payment_delta = value

    @property
    def next_payment_date(self):
        return self.payment_date

    @next_payment_date.setter
    def next_payment_date(self, value):
        self._type_check(value, date)
        self.payment_date = value

    @property
    def previous_payment_date(self):
        return self.next_payment_date - self.payment_delta

    @property
    def daily_rate(self):
        return self.amount / (self.next_payment_date - self.previous_payment_date).days

    @property
    def weekly_rate(self):
        return self.daily_rate * 7

    @property
    def montyhly_rate(self):
        pass
