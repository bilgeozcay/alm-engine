from periodicity import Periodicity
from amortizationtype import AmortizationType
from amortization import Amortization
from cashflow import Cashflow
from cashflow import CashflowType
from datetime import date
from dateutil import relativedelta

class CashflowEngine:

    def generate_amortization_schedule(self, transaction):

        amortization = []

        if transaction.amortization_type == AmortizationType.BULLET:
            amortization.append(Amortization(transaction.maturity_date, 1))
            return amortization

        elif transaction.amortization_type == AmortizationType.LINEAR:
            start_date = transaction.value_date
            end_date = transaction.maturity_date
            month_count = transaction.amortization_periodicity.value

            current_date = start_date

            while current_date < end_date:

                next_date = current_date + relativedelta.relativedelta(months=month_count)

                if next_date <= end_date:
                    current_date = next_date
                else:
                    current_date = end_date
                
                amortization.append(Amortization(current_date, 0))


            i = 0
            length = len(amortization)

            while i < length:
                amortization[i].percentage = 1/length
                i += 1
    
            return amortization

        else:
            return 0

    def generate_principal_cashflows(self,transaction):


        amortization_schedule = self.generate_amortization_schedule(transaction)

        cashflows = []

        i = 0
        while i<len(amortization_schedule):
            date = amortization_schedule[i].date
            percentage = amortization_schedule[i].percentage
            amount = transaction.nominal * percentage
            cashflows.append(Cashflow(CashflowType.PRINCIPAL, date, date, date, amount))
            i += 1
        
        return cashflows

    def generate_interest_cashflows(self, transaction):
        return 0