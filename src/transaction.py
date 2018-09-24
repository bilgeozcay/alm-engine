

class Transaction:

    def __init__(self, nominal, value_date, maturity_date, interest_type, interest_rate, interest_periodicity, amortization_type, amortization_periodicity):
        self.nominal = nominal
        self.value_date = value_date
        self.maturity_date = maturity_date
        self.interest_type = interest_type
        self.interest_rate = interest_rate
        self.amortization_type = amortization_type
        self.amortization_periodicity = amortization_periodicity
        self.interest_periodicity = interest_periodicity
