class Amortization:

    def __init__(self, date, percentage):
        self.date = date
        self.percentage = percentage

    def __str__(self):
        return str(self.date) + ":" + str(round(self.percentage, 4))
    