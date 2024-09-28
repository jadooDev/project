import re
from  dataProcessing import categories
# Simple rule-based categorization


def categorize_transaction(transaction_name):
    for category, keywords in categories.items():
        if any(re.search(keyword, transaction_name, re.IGNORECASE) for keyword in keywords):
            return category
    return 'Other'

def categorize_transactions(transactions):
    categorized_data = []
    for transaction in transactions:
        category = categorize_transaction(transaction['name'])
        categorized_data.append({
            'name': transaction['name'],
            'amount': transaction['amount'],
            'category': category
        })
    return categorized_data