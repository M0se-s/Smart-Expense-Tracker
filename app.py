import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Import your custom AI module
from ai_engine import auto_categorize

# 1. Configuration and Data Loading
CSV_FILE = "Expense_data_1.csv"

if os.path.exists(CSV_FILE):
    data = pd.read_csv(CSV_FILE)
else:
    # If the file gets deleted, rebuild it with the exact correct columns
    data = pd.DataFrame(
        columns=["Date", "Category", "Note", "Amount", "Income/Expense"]
    )

# 2. UI Layout: Header
st.title("Smart Expense Tracker Dashboard")

# 3. UI Layout: Input Form
st.subheader("Add New Transaction")
with st.form("expense_form", clear_on_submit=True):
    date = st.date_input("Date")
    note = st.text_input("Note (e.g., Shawarma, Uber)")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    exp_type = st.selectbox("Type", ["Expense", "Income"])

    submitted = st.form_submit_button("Save Transaction")

    if submitted and note:
        # Trigger the AI only for expenses. Income doesn't need AI.
        category = "Income"
        if exp_type == "Expense":
            category = auto_categorize(note)

        # Format the new entry to perfectly match the database
        new_row = pd.DataFrame(
            [
                {
                    "Date": date.strftime("%Y-%m-%d"),
                    "Category": category,
                    "Note": note,
                    "Amount": amount,
                    "Income/Expense": exp_type,
                }
            ]
        )

        # Append to memory, save to disk, and refresh the UI
        data = pd.concat([data, new_row], ignore_index=True)
        data.to_csv(CSV_FILE, index=False)
        st.success(f"Successfully added '{note}' under category: {category}")
        st.rerun()

# 4. UI Layout: Data Table
st.subheader("Transaction History")
st.dataframe(data)

# 5. UI Layout: Visualizations
expenses_only = data[data["Income/Expense"] == "Expense"]

if not expenses_only.empty:
    st.subheader("Expense Breakdown")

    # Split the screen into two equal columns
    col1, col2 = st.columns(2)
    category_totals = expenses_only.groupby("Category")["Amount"].sum()

    with col1:
        fig, ax = plt.subplots()
        category_totals.plot(kind="bar", color="skyblue", edgecolor="black", ax=ax)
        ax.set_ylabel("Amount Spent")
        ax.set_title("Total by Category")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col2:
        fig2, ax2 = plt.subplots()
        category_totals.plot.pie(autopct="%1.1f%%", startangle=90, shadow=True, ax=ax2)  # type: ignore
        ax2.set_ylabel("")
        st.pyplot(fig2)
