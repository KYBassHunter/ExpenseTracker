import datetime

class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.categories = set()

    def add_income(self, amount):
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Income must be a positive number.")
            self.income += amount
            print(f"Income of ${amount:.2f} added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def add_expense(self, description, amount, category):
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Expense amount must be a positive number.")
            self.expenses.append({"description": description, "amount": amount, "category": category})
            self.categories.add(category)
            print(f"Expense of ${amount:.2f} for {description} added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def get_total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def get_remaining_budget(self):
        return self.income - self.get_total_expenses()

    def get_expenses_by_category(self):
        category_expenses = {}
        for category in self.categories:
            category_expenses[category] = sum(expense["amount"] for expense in self.expenses if expense["category"] == category)
        return category_expenses

    def display_budget_overview(self):
        print("\n===== Budget Overview =====")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${self.get_total_expenses():.2f}")
        print(f"Remaining Budget: ${self.get_remaining_budget():.2f}")
        print("\nExpenses by Category:")
        for category, amount in self.get_expenses_by_category().items():
            print(f"  {category}: ${amount:.2f}")

def main():
    budget = BudgetTracker()
    
    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget Overview")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            amount = input("Enter income amount: $")
            budget.add_income(amount)
        elif choice == "2":
            description = input("Enter expense description: ")
            amount = input("Enter expense amount: $")
            category = input("Enter expense category: ")
            budget.add_expense(description, amount, category)
        elif choice == "3":
            budget.display_budget_overview()
        elif choice == "4":
            print("Thank you for using the Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()