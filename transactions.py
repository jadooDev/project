import random
from datetime import datetime, timedelta

categories = ['Food', 'Transport', 'Entertainment', 'Shopping', 'Bills', 'Others']

transactions = []

# Create 10 random transactions
for _ in range(10):
    transaction = {
        'User': f'Transaction {_}',
        'Amount': round(random.uniform(5, 200), 2),
        'Category': random.choice(categories),
        'Date': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
    }
    transactions.append(transaction)

print(transactions)