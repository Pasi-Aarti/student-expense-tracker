import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter Category (Food/Travel/Books/Rent/Other): ").strip().title()
    description = input("Enter short description (e.g., Bus pass, Lunch): ").strip()
    
    try:
        amount = float(input("Enter Amount (₹): "))
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value for amount.")
        return

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, f"{amount:.2f}"])
    
    print("✅ Expense saved successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("📂 No records found.")
        return

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            print("📂 No expenses recorded yet.")
            return

        print("\n" + "="*65)
        print(f"{'ID':<4} | {'Date':<12} | {'Category':<12} | {'Description':<18} | {'Amount':<10}")
        print("="*65)
        for idx, row in enumerate(reader[1:], start=1):
            print(f"{idx:<4} | {row[0]:<12} | {row[1]:<12} | {row[2]:<18} | ₹{row[3]:<10}")
        print("="*65)

def category_summary():
    if not os.path.exists(FILE_NAME):
        print("📂 No records found.")
        return

    summary = {}
    total = 0.0

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        for row in reader:
            cat = row[1]
            amt = float(row[3])
            summary[cat] = summary.get(cat, 0.0) + amt
            total += amt

    if not summary:
        print("📂 No data available for summary.")
        return

    print("\n--- 📊 Category-Wise Expense Summary ---")
    for cat, amt in summary.items():
        print(f"• {cat:<15}: ₹{amt:.2f}")
    print("-" * 38)
    print(f"💰 Grand Total   : ₹{total:.2f}")

def delete_expense():
    view_expenses()
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        return

    try:
        del_id = int(input("\nEnter the ID of the expense to delete (0 to cancel): "))
        if del_id == 0:
            return
        if 1 <= del_id < len(rows):
            removed = rows.pop(del_id)
            with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"🗑️ Deleted: {removed[2]} (₹{removed[3]})")
        else:
            print("❌ Invalid ID.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    initialize_file()
    while True:
        print("\n=== 🎓 STUDENT EXPENSE TRACKER PRO ===")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Category Summary & Total")
        print("4. Delete an Expense")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("👋 Goodbye! Data saved in 'expenses.csv'.")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()1
    