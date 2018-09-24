from interesttype import InterestType
from periodicity import Periodicity
from amortizationtype import AmortizationType
from transaction import Transaction
from cashflowengine import CashflowEngine
from datetime import date
from datetime import datetime


start = datetime.now()
print("STARTING at:\t" + str(start))

#Create 100000 transactions
n = 1000
transactions = []


value_date = date(2018, 9, 23)
maturity_date = date (2020, 9, 30)
interest_type = InterestType.FIXED
interest_rate = 0.06
amort_type = AmortizationType.LINEAR
amort_period = Periodicity.MONTHLY
interest_period = Periodicity.MONTHLY

i=0
while i<n:
    transactions.append(Transaction(100000, value_date, maturity_date, interest_type, interest_rate, interest_period, amort_type, amort_period))
    e = CashflowEngine()
    e.generate_principal_cashflows(transactions[i])
    i+=1

    if i%1000 == 0:
        print("processed so far:\t" + str(i))


#i = 0
#while i < len(p_cashflows):
#    print(p_cashflows[i])
#    i += 1

end = datetime.now()
print("ENDING at:\t" + str(end))

diff = end - start
print("IT TOOK:\t" + str(diff.total_seconds()) + "seconds.")