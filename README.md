# 💼 BCG GenAI Job Simulation: Simple Financial-Analysis Chatbot

This project was completed as part of **The Forage – BCG (Boston Consulting Group) GenAI Job Simulation**.  
It demonstrates how generative AI and data analysis can automate financial insights using a simple chatbot built with Flask and Pandas.

---

## 🧠 Overview
This prototype is a lightweight **Flask web app** that reads a CSV file (`financial_data.csv`) and answers three predefined business questions related to company performance.

---

## 💬 Predefined Queries & Answers
1. **What is the total revenue?**  
   → Returns the sum of the **Total Revenue** column.

2. **How has net income changed over the last year?**  
   → Compares the last two rows in the **Net Income** column and reports the absolute change.

3. **What percentage of revenue is spent on Selling, General & Administrative (SG&A)?**  
   → Calculates SG&A spend as a percentage of total revenue.

---

## ⚙️ How to Run Locally
1. Make sure you have Python installed.  
2. Install required dependencies:
   ```bash
   pip install flask pandas
