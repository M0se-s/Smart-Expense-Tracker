# Smart Expense Tracker

A Python **expense tracker + dashboard** that stores transactions in a CSV file, visualizes spending by category, and can **auto-categorize expenses** using the **Gemini API**.

## What it does
- Add **Income** or **Expense** transactions (date, note, amount)
- Automatically assigns an expense category using AI (Gemini) based on the note text
- Saves everything to a CSV “database”
- Shows a dashboard with:
  - Transaction history table
  - Bar chart: total spend by category
  - Pie chart: category distribution

## Tech Stack
- Python
- Streamlit (UI)
- Pandas (data handling)
- Matplotlib (charts)
- Google Gemini (`google-genai`) for categorization
- `python-dotenv` for environment variables

## Project Files
- `app.py` — Streamlit app (main UI/dashboard)
- `ai_engine.py` — Gemini-based categorizer (`auto_categorize(note)`)
- `dashboard.py` — matplotlib dashboard helper (plots)
- `main.py` — script-style demo using sample CSV data + plotting
- `Expense_data_1.csv` — default CSV used by the Streamlit app
- `Sample Expense Data.csv` — sample dataset used by `main.py`

## Categories (AI)
The AI categorizer returns **exactly one** of:
- `Food`
- `Subscriptions`
- `Transportation`
- `Entertainment`
- `Other`

## Setup

### 1) Clone the repo
```bash
git clone https://github.com/M0se-s/Smart-Expense-Tracker.git
cd Smart-Expense-Tracker
```

### 2) Install dependencies
If you don’t have a `requirements.txt` yet, install manually:
```bash
pip install streamlit pandas matplotlib python-dotenv google-genai
```

### 3) Configure your Gemini API key
This project loads environment variables via `python-dotenv`.

Create a `.env` file in the repo root and add:
```env
GEMINI_API_KEY=your_api_key_here
```

## Run the Streamlit App (Recommended)
```bash
streamlit run app.py
```

The app:
- reads/writes `Expense_data_1.csv`
- auto-categorizes *expenses* (income is labeled as `Income`)
- renders charts from your stored transactions

## Run the Script Demo (Optional)
`main.py` reads `Sample Expense Data.csv` and generates plots:
```bash
python main.py
```

## Notes
- If the Gemini API call fails, the app will fall back to category `Other`.
- CSV columns used by the project:
  - `Date`, `Category`, `Note`, `Amount`, `Income/Expense`
