import json
import matplotlib.pyplot as plt
from datetime import datetime

FILENAME = "expenses.json"

def load_expenses():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=4)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Transport, etc.): ")
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    expense = {"amount": amount, "category": category, "date": date}
    data = load_expenses()
    data.append(expense)
    save_expenses(data)
    print("Expense added!")

def show_summary():
    data = load_expenses()
    summary = {}
    for entry in data:
        month = entry["date"][:7]
        cat = entry["category"]
        summary.setdefault(month, {}).setdefault(cat, 0)
        summary[month][cat] += entry["amount"]

    for month, cats in summary.items():
        print(f"\nMonth: {month}")
        for cat, total in cats.items():
            print(f"  {cat}: ₹{total:.2f}")

def plot_chart():
    data = load_expenses()
    cat_total = {}
    for entry in data:
        cat = entry["category"]
        cat_total[cat] = cat_total.get(cat, 0) + entry["amount"]

    plt.pie(cat_total.values(), labels=cat_total.keys(), autopct='%1.1f%%')
    plt.title("Expense Breakdown by Category")
    plt.show()

def main():
    while True:
        print("\n1. Add Expense\n2. Show Summary\n3. Plot Chart\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            plot_chart()
        elif choice == '4':
            break

main()