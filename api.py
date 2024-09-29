from flask import Flask, request, jsonify
from transactions import transactions
from expenseCategorization import categorize_transactions
from dataAndAnalytics import calculate_monthly_spending, generate_insights
from monthlyReport import generate_monthly_report

app = Flask(__name__)

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions), 200

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    transaction_data = request.json
    transactions.append(transaction_data)  # Add transaction to the list
    return jsonify({"message": "Transaction added successfully!"}), 201

@app.route('/api/monthly-spending', methods=['GET'])
def get_monthly_spending():
    categorized_transactions = categorize_transactions(transactions)
    monthly_spending = calculate_monthly_spending(categorized_transactions)
    return jsonify(monthly_spending), 200

@app.route('/api/report', methods=['GET'])
def get_report():
    categorized_transactions = categorize_transactions(transactions)
    monthly_spending = calculate_monthly_spending(categorized_transactions)
    report = generate_monthly_report(monthly_spending)
    return jsonify({"report": report}), 200

@app.route('/api/insights', methods=['GET'])
def get_insights():
    categorized_transactions = categorize_transactions(transactions)
    monthly_spending = calculate_monthly_spending(categorized_transactions)
    insights = generate_insights(monthly_spending)
    return jsonify({"insights": insights}), 200

if __name__ == '__main__':
    app.run(debug=True)