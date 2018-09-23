from enum import Enum, auto


class CashFlowType(Enum):
    INTEREST = auto()
    PRINCIPAL = auto()


class Cashflow:
    def __init__(self, type, from_date, to_date, payment_date, amount):
        self.type = type
        self.from_date = from_date
        self.to_date = to_date
        self.payment_date = payment_date
        self.amount = amount
    


