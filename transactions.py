import random
from datetime import datetime, timedelta

categories = {
    'Food': ['restaurant', 'grocery'],
    'Transport': ['uber', 'taxi', 'bus'],
    'Entertainment': ['cinema', 'movie', 'theater'],
    'Shopping': ['amazon', 'shop', 'store'],
    'Bills': ['electricity', 'water', 'rent'],
    'Others': []
}

transactions = []

# Create 10 random transactions
for _ in range(1000):
    transaction = {
        'name': f'Transaction {_}',
        'amount': round(random.uniform(5, 200), 2),
        'category': random.choice(list(categories.keys())),
        'date': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
    }
    transactions.append(transaction)