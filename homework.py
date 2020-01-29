import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = int(limit)
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        return self.records

    def get_today_stats(self):
        stats_today = sum([record.amount for record in self.records if record.date == dt.datetime.now().date()])
        return stats_today

    def get_week_stats(self):
        today = dt.datetime.now().date()
        week = dt.timedelta(days=7)
        last_week = today - week
        stats_for_last_week = sum([record.amount for record in self.records if last_week <= record.date <= today])
        return stats_for_last_week


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_today = self.get_today_stats()
        free_calories = self.limit - calories_today
        if free_calories > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {free_calories} кКал"
        return "Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 61.06
    EURO_RATE = 67.90

    def get_today_cash_remained(self, currency):
        limit_today = self.limit
        balance_today = self.get_today_stats()
        balance = limit_today - balance_today
        balance_all_currency = {
            "rub": (1, "руб", None),
            "usd": (self.USD_RATE, "USD", 2),
            "eur": (self.EURO_RATE, "Euro", 2)
        }
        balance_in_currency, value_currency, how_round = balance_all_currency[currency]
        if balance_today == limit_today:
            return "Денег нет, держись"
        if balance_today < limit_today:
            return f"На сегодня осталось {round(balance/balance_in_currency, how_round)} {value_currency}"
        return f"Денег нет, держись: твой долг - {-round(balance/balance_in_currency, how_round)} {value_currency}"

class Record: 
     def __init__(self, amount, comment, date=None): 
         self.amount = amount 
         self.comment = comment 
         if date == None: 
             self.date = dt.datetime.today().date() 
         else: 
             self.date = dt.datetime.strptime(date, '%d.%m.%Y').date() 