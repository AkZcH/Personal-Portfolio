class Income:
    def __init__(self, source, amount):
        self.source = source
        self.amount = amount

    def get_source(self):
        return self.source

    def get_amount(self):
        return self.amount

    def __str__(self):
        return f"{self.source}: ${self.amount}"

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def get_category(self):
        return self.category

    def get_amount(self):
        return self.amount

    def __str__(self):
        return f"{self.category}: ${self.amount}"

class IncomeExpenseTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_income(self):
        total = 0
        for income in self.incomes:
            total += income.get_amount()
        return total

    def get_total_expenditure(self):
        total = 0
        for expense in self.expenses:
            total += expense.get_amount()
        return total

    def get_net_balance(self):
        return self.get_total_income() - self.get_total_expenditure()

    def __str__(self):
        result = f"Total Income: ${self.get_total_income()}\n"
        result += f"Total Expenditure: ${self.get_total_expenditure()}\n"
        result += f"Net Balance: ${self.get_net_balance()}\n"

        result += "Incomes:\n"
        for income in self.incomes:
            result += f"{income}\n"

        result += "Expenses:\n"
        for expense in self.expenses:
            result += f"{expense}\n"

        return result