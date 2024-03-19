class RentalPropertyCalculator:
    def __init__(self):
        self.income_sources = {}
        self.expense_items = {}
        self.total_investment = 0

    def add_income_source(self, name, amount):
        self.income_sources[name] = amount

    def add_expense_item(self, name, amount):
        self.expense_items[name] = amount

    def set_total_investment(self, amount):
        self.total_investment = amount

    def calculate_total_income(self):
        return sum(self.income_sources.values())

    def calculate_total_expenses(self):
        return sum(self.expense_items.values())

    def calculate_cash_flow(self):
        return self.calculate_total_income() - self.calculate_total_expenses()

    def calculate_annual_cash_flows(self):
        return self.calculate_cash_flow() * 12

    def calculate_roi(self):
        annual_cash_flows = self.calculate_annual_cash_flows()
        if self.total_investment == 0:
            return 0
        return (annual_cash_flows / self.total_investment) * 100

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    calculator = RentalPropertyCalculator()

    while True:
        print('Welcome to Bigger Pockets. Type "quit" at any point to exit.')
        name = input("Enter the name of the income source (or 'done' to finish): ")
        if name.lower() in ['done', 'quit']:
            if name.lower() == 'quit':
                return
            break
        amount = get_float_input(f"Enter the amount for {name}: $")
        calculator.add_income_source(name, amount)

    while True:
        name = input("Enter the name of the expense item (or 'done' to finish): ")
        if name.lower() in ['done', 'quit']:
            if name.lower() == 'quit':
                return 'thanks for visting us'
            break
        amount = get_float_input(f"Enter the amount for {name}: $")
        calculator.add_expense_item(name, amount)

    total_investment = get_float_input("Enter the total investment amount: $")
    calculator.set_total_investment(total_investment)

    print(f"Monthly Cash Flow: ${calculator.calculate_cash_flow()}")
    print(f"Annual Cash Flows: ${calculator.calculate_annual_cash_flows()}")
    print(f"ROI: {calculator.calculate_roi()}%")


main()