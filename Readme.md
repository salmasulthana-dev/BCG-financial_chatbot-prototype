# BCG Gen-AI Job-Sim: Simple Financial-Analysis Chatbot

## Overview
This prototype is a stripped-down Flask web app that answers three predefined financial questions using the CSV file analysed in Task 1.

## Predefined Queries & Answers
1. **What is the total revenue?**  
   Returns the sum of the “Revenue” column.

2. **How has net income changed over the last year?**  
   Compares the last two rows in the “Net Income” column and reports the absolute change.

3. **What percentage of revenue is spent on Selling, General & Administrative?**  
   Calculates SG&A spend as a percentage of total revenue.

## How to Run
1. Ensure `flask` and `pandas` are installed:  
   ```bash
   pip install flask pandas