"""
BCG Gen-AI Job-Sim: Simple Financial-Analysis Chatbot
Reads 'financial_data.csv' and answers three predefined questions.
"""

from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import os

# -------------------------------------------------
# 1. Load CSV (must be in same folder)
# -------------------------------------------------
CSV_NAME = "financial_data.csv"
if not os.path.exists(CSV_NAME):
    raise FileNotFoundError(f"{CSV_NAME} must be in the same folder as chatbot.py")

df = pd.read_csv(CSV_NAME)

# -------------------------------------------------
# 2. Extract answers
# -------------------------------------------------
TOTAL_REVENUE = df["Total Revenue"].sum()

# Year-over-year net-income change
NET_INCOME_LAST_YEAR = df["Net Income"].iloc[-2]
NET_INCOME_THIS_YEAR = df["Net Income"].iloc[-1]
NET_INCOME_CHANGE = NET_INCOME_THIS_YEAR - NET_INCOME_LAST_YEAR

# -------------------------------------------------
# 3. Canned responses
# -------------------------------------------------
ANSWERS = {
    "What is the total revenue?":
        f"The total revenue is ${TOTAL_REVENUE:,.0f}.",

    "How has net income changed over the last year?":
        f"The net income has {'increased' if NET_INCOME_CHANGE >= 0 else 'decreased'} "
        f"by ${abs(NET_INCOME_CHANGE):,.0f} over the last year.",

    "What percentage of revenue is spent on Selling, General & Administrative?":
        "SG&A data is not available in this dataset."
}

# -------------------------------------------------
# 4. Flask web app (single file)
# -------------------------------------------------
app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<title>BCG Chatbot Prototype</title>
<h2>Financial-Analysis Chatbot</h2>
<form action="/ask" method="post">
    <label>Select a predefined question:</label><br>
    <select name="query" required>
      {% for q in queries %}
        <option value="{{ q }}">{{ q }}</option>
      {% endfor %}
    </select><br><br>
    <input type="submit" value="Ask">
</form>
{% if answer %}
<p><strong>Answer:</strong> {{ answer }}</p>
{% endif %}
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE, queries=list(ANSWERS.keys()))

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("query", "")
    answer = ANSWERS.get(question,
                         "Sorry, I can only provide information on predefined queries.")
    return render_template_string(HTML_PAGE,
                                  queries=list(ANSWERS.keys()),
                                  answer=answer)

if __name__ == "__main__":
    app.run(debug=True)