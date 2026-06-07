# # Expense Tracker
# # Built by: Nikita
# print("Expense Tracker")

# expenses = [
    
# ]
# while True:
#     print("option 1: Add Expense" )
#     print("option 2: View Expenses")
#     print("option 3: Goodbye")
#     print("option 4: Total Expenses")
    
#     choice = input("Enter your choice: ")
#     print("-" * 30)
#     # OPTION 1: ADD EXPENSE
#     if choice == "1":
#         description = input("Enter expense description: ")
#         amount = float(input("Enter expense amount: "))
#         category = input("Enter expense category: ")
#         expense= {
#             "description": description,
#             "amount": amount,
#             "category": category
#         }
#         expenses.append(expense)
#         print("Expense added successfully!")
#         print("-" * 30)

#         # OPTION 2: VIEW EXPENSES
#     elif choice == "2":
#         if len(expenses) == 0:
#             print("No expenses to show.")
#         else: 
#             print("Your Expenses:")
#             for expense in expenses:
#                 print(f"- {expense['description']} | {expense['category']} | ${expense['amount']}")
#             print("-" * 30)

#     # OPTION 3: GOODBYE
#     elif choice == "3":
#         print("Goodbye!")
#         print("-" * 30)
#         break

#     # OPTION 4: TOTAL EXPENSES
#     elif choice == "4":
#        if len(expenses) == 0:
#             print("No expenses to calculate.")
#        else:
#         #    ----total count ---
#         print(f"Total expenses: {len(expenses)}")

#         # ----total spent (loop 1)---
#         total_spent = 0
#         for expense in expenses:
#             total_spent += expense['amount']
#         print(f"Total spent: ${total_spent}")

#         #--- grup by category(loop 2 seperate) ---
#         by_category = {}
#         for expense in expenses:
#             category = expense['category']
#             if category not in by_category:
#                 by_category[category] = 0
#             by_category[category] += expense['amount']

#         # ==print breakdown(loop3, seperate) 
#         print("Expenses by Category:")
#         for category, total in by_category.items():
#             print(f"- {category}: ${total}")

#         print("-" * 30)
#     else:
#         print("Invalid choice. Please try again.")

# NEW VERSIONWITH FUNCTIONS

# EXPENSE TRACKER
# BUILT BY: NIKITA
import csv
import os

FILENAME = "expenses.csv"

def save_expenses(expenses):
    # saves all expenses to a csv file

    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["description", "amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"saved {len(expenses)} expenses to {FILENAME}")

def load_from_csv():
    expenses = []

    if not os.path.exists(FILENAME):
        print(f"No existing expenses found. Starting fresh.")
        return expenses
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
        print(f"Loaded {len(expenses)} expenses from {FILENAME}")
        
        return expenses
def is_valid_amount(value):
    try:
        return float(value) > 0
    except ValueError:
        return False
    
def create_expense(description, amount, category):
    return {
        "description": description,
        "amount": float(amount),
        "category": category
    }

def add_expense(expenses):
    description = input("Description: ")
    amount_input = input("Amount: ")

    if not is_valid_amount(amount_input):
        print("Invalid amount. Please enter a positive number.")
        return
    
    category = input("Category: ")
    expense = create_expense(description, amount_input, category)
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
    else:
        print("\nYour Expenses:")
        for i, expenses in enumerate(expenses, start=1):
            print(f"  {i}. {expenses['description']} |"
                  f" {expenses['category']} |"
                  f" ${expenses['amount']}")
            
def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    total_spent = sum(float(expense['amount']) for expense in expenses)
    print(f"\n{'-'* 30}")
    print(f"   total expenses: {len(expenses)}")
    print(f"   total spent: ${total_spent:.2f}")

    by_category = {}
    for expense in expenses:
        cat = expense['category']
        by_category[cat] = by_category.get(cat, 0) + expense['amount']

    print("\nExpenses by Category:")
    for cat, total in by_category.items():
        print(f"  {cat}: ${total:.2f}")
    print(f"{'-' * 30}")


def main():

    expenses= load_from_csv()

    while True:
        print("\nOptions:")
        print("  1. Add Expense")
        print("  2. View Expenses")
        print("  3. Show Summary")
        print("  4. Exit")
        print("  5. Save & Quit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "5":
            save_expenses(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()