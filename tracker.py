import pandas as pd

df = pd.read_csv("Sample Expense Data.csv")
data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]


# Load and clean the initial data
def add_expense(date, category, note, amount, exp_type="Expense"):
    global data

    new_entry = pd.DataFrame(
        [
            {
                "Date": date,
                "Category": category,
                "Note": note,
                "Amount": amount,
                "Income/Expense": exp_type,
            }
        ]
    )

    data = pd.concat([data, new_entry], ignore_index=True)
    print(f"Added: {note} - {amount} ({category})")


# Add expense
def view_expenses(n=5):
    return data.tail(n)


# Summarize expense data
def summarize_expenses(by="Category"):
    summary = data[data["Income/Expense"] == "Expense"].groupby(by)["Amount"].sum()
    return summary.sort_values(ascending=False)


# Add the weekend expenses
print("\n--- ADDING NEW EXPENSES ---")
add_expense("2025-08-22 19:30", "Food", "Shawarma", 2500, "Expense")
add_expense(
    "2025-08-23 08:00", "Subscriptions", "Netflix Monthly Plan", 4500, "Expense"
)
add_expense(
    "2025-08-24 14:00", "Entertainment", "Outdoor Games with friends", 7000, "Expense"
)

print("\n--- LAST 5 TRANSACTIONS ---")
print(view_expenses(5))

print("\n--- SPENDING SUMMARY BY CATEGORY ---")
print(summarize_expenses())
