import datetime
from collections import defaultdict

#Calculate monthly expenses
def calculate_monthly_spending(transactions):
    monthly_spending = defaultdict(lambda: defaultdict(float))

    for txn in transactions: 
        txn_date = datetime.datetime.strptime(txn['date'], '%Y-%m-%d')
        month = txn_date.strftime('%Y-%m')
        monthly_spending[month][txn['category']] += txn['amount']
        
# Generate insights, e.g., spending trend comparison
def generate_insights(monthly_spending):
    insights = []
    months = sorted(monthly_spending.keys()) #month list assorted in ascending order (comparisson is chronological)

    for i in range(1, len(months)): #compares month to previous starting from second month
        prev_month, current_month = months[i-1], months[i] # Declares variables for previous month and current month
        for category in monthly_spending[current_month]: #Loop over each category for current month
            current_spend = monthly_spending[current_month][category] # Declare a variable 
            prev_spend = monthly_spending[prev_month].get(category, 0)

            if current_spend > prev_spend:
                insights.append(f"Your spending on {category} increased by {current_spend - prev_spend:.2f} compared to last month.")
            elif current_spend < prev_spend:
                insights.append(f"Good job! You reduced your {category} spending by {prev_spend - current_spend:.2f} this month.")

    return insights