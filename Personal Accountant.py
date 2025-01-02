import csv
from datetime import datetime

EXPENSES_FILE = "expenses.csv"

def read_expenses():
    try:
        with open(EXPENSES_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return [] 

def write_expense(amount, category, description, date):
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        fieldnames = ['date', 'amount', 'category', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({'date': date,'amount': amount,'category': category,'description': description})

def delete_all_expenses():
    confirmation = input("Are you sure you want to delete all expenses? (y/n): ").lower()
    if confirmation == 'y':
        try:
            with open(EXPENSES_FILE, mode='w', newline='') as file:
                fieldnames = ['date', 'amount', 'category', 'description']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
            print("All expenses have been deleted.\n")
        except Exception as e:
            print(f"Error deleting expenses: {e}")
    else:
        print("Deletion canceled.\n")

def track_expense():
    print("\n--- Track New Expense ---")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (e.g., food, entertainment, transport,other): ").lower()
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_expense(amount, category, description, date)
    print("Expense added successfully!\n")

def display_expenses():
    expenses = read_expenses()
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return
    print("\n--- All Expenses ---")
    for expense in expenses:
        print(f"{expense['date']} - ₹{expense['amount']} - {expense['category']} - {expense['description']}")
    print()

def display_summary():
    expenses = read_expenses()
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    summary = {}
    
    for expense in expenses:
        category = expense['category']
        amount = float(expense['amount'])
        
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    
    print("\n--- Expense Summary ---")
    for category, total in summary.items():
        print(f"{category.capitalize()}: ₹{total:.2f}")
    print()

def main():
    print("Welcome I am your Personal Accountant\n")
    while True:
        print("Options:")
        print("1. Track new expense")
        print("2. View all expenses")
        print("3. View expense summary by category")
        print("4. Delete all expenses")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            track_expense()
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            display_summary()
        elif choice == '4':
            delete_all_expenses()
        elif choice == '5':
            print("Thank you for trusting me with your expenses")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
