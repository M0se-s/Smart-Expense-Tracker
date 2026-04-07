import matplotlib.pyplot as plt


def generate_dashboard(data):
    """Generates visual dashboards (Pie and Bar charts) for expense distribution.
    Filters out income to ensure accurate expense representation."""

    expense_data = data[data["Income/Expense"] == "Expense"]
    expense_summary = expense_data.groupby("Category")["Amount"].sum()

    if expense_summary.empty:
        print("No expense data available to plot.")
        return

    # Pie Chart
    plt.figure(figsize=(6, 6))
    expense_summary.plot.pie(autopct="%1.1f%%", startangle=90, shadow=True)
    plt.title("Expenses Breakdown by Category")
    plt.ylabel("")

    # Bar Chart
    plt.figure(figsize=(8, 5))
    expense_summary.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Total Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation = 45)
    
    plt.show()
    
    
