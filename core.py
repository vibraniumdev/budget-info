from datetime import date
import calendar


class Calculator:
    def __init__(self):
        self.today = date.today().day
        self.this_month = date.today().month
        # self.last_monthday = calendar.monthrange(date.today().year, date.today().month)

    def last_monthday(self):
        return calendar.monthrange(self.today, self.this_month)[1]

    def days_left(self):
        return self.last_monthday()

    def get_money(self):
        return float(input("Dinheiro (R$): \n"))

    # @staticmethod
    # def get_money():
    #     return float(input("Dinheiro (R$): \n"))

    # def calculate_budget(self):
    #     return self.get_money - self.days_left


budget = Calculator()


# print(f"Hoje é dia: {teste.today}")
# print(f"Mês atual: {teste.this_month}")

# def pick_today():
#     return date.today().day


# def actual_month():
#     return date.today().month

# def last_day():
#     weekday, last_day = calendar.monthrange(date.today().year, actual_month())
#     return last_day

# def days_left(last_day):
#     return last_day - pick_today()


# def get_money():
#     amount = float(input("Quantidade de dinheiro: \n"))
#     return amount


# def calculate_budget(money_amount, present_day, days_left):
#     sugested_budget = f"Quantidade sugerida de dinheiro gasto por dia: R$ {(money_amount / days_left):.2f}"
#     return sugested_budget


# print(f"Dias para terminar o mês: {days_left(last_day())}")

# print(calculate_budget(get_money(), pick_today(), days_left(last_day())))
