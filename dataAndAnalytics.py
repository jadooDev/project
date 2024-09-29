import datetime
from collections import defaultdict

#Calculate monthly expenses
def calculate_monthly_spending(transactions):
    monthly_spending = defaultdict(lambda: defaultdict(float)) # defaultdict creates dictionary where each month maps to a category dictionary initialized to 0.0

    for txn in transactions: # loop that iterates over list of transactions
        txn_date = datetime.datetime.strptime(txn['date'], '%Y-%m-%d') # convert the string of the transaction's date into datetime object
        month = txn_date.strftime('%Y-%m') # extracts year and month from txn_date and convert it to a datetime object
        monthly_spending[month][txn['category']] += txn['amount'] #update monthly_spending to accumulate the total amount spent in that month
        
# Generate insights
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
    
        # Prepare a list to store total monthly spending
    monthly_totals = {month: sum(categories.values()) for month, categories in monthly_spending.items()}

    # Iterate through the monthly totals to compare with the previous month
    for i, month in enumerate(monthly_totals):
        if i > 0:  # Skip the first month since there's no previous month to compare to
            previous_month = list(monthly_totals.keys())[i - 1]
            current_spending = monthly_totals[month]
            previous_spending = monthly_totals[previous_month]
            
            # Calculate percentage change
            if previous_spending > 0:
                percentage_change = ((current_spending - previous_spending) / previous_spending) * 100
            else:
                percentage_change = 100 if current_spending > 0 else 0  # Handle edge case
            
            # Generate insights for total spending comparison
            if percentage_change > 0:
                insights.append(f"In {month}, you spent ${current_spending:.2f}, which is an increase of {percentage_change:.2f}% compared to {previous_month}.")
            elif percentage_change < 0:
                insights.append(f"In {month}, you spent ${current_spending:.2f}, which is a decrease of {abs(percentage_change):.2f}% compared to {previous_month}.")
            else:
                insights.append(f"In {month}, you spent the same amount as in {previous_month}: ${current_spending:.2f}.")

            # Compare spending by categories
            for category in monthly_spending[month]:
                current_amount = monthly_spending[month].get(category, 0)
                previous_amount = monthly_spending[previous_month].get(category, 0)
                
                if previous_amount > 0:
                    category_percentage_change = ((current_amount - previous_amount) / previous_amount) * 100
                else:
                    category_percentage_change = 100 if current_amount > 0 else 0
                
                if category_percentage_change > 0:
                    insights.append(f"  - In {month}, you spent ${current_amount:.2f} on {category}, which is an increase of {category_percentage_change:.2f}% from {previous_month}.")
                elif category_percentage_change < 0:
                    insights.append(f"  - In {month}, you spent ${current_amount:.2f} on {category}, which is a decrease of {abs(category_percentage_change):.2f}% from {previous_month}.")
                else:
                    insights.append(f"  - In {month}, you spent the same amount on {category} as in {previous_month}: ${current_amount:.2f}.")

    return insights

    