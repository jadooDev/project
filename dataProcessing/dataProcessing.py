import pandas as pd

# Sample data: Date, User, Description, and Amount
data = {
    'Date': ['2024-09-01', '2024-09-03', '2024-09-04', '2024-09-05', '2024-09-07', '2024-09-08',
             '2024-09-01', '2024-09-04', '2024-09-06', '2024-09-09'],
    'User': ['Alice', 'Alice', 'Alice', 'Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob', 'Bob'],
    'Description': ['Groceries', 'Uber Ride', 'Rent Payment', 'Dining Out', 'Gas Station', 'Netflix Subscription',
                    'Groceries', 'Rent Payment', 'Gym Membership', 'Spotify Subscription'],
    'Amount': [120, 30, 800, 45, 60, 15, 110, 800, 50, 12]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define categories based on Description, including Rent and Subscriptions
def categorize_expense(description):
    if 'Groceries' in description:
        return 'Food'
    elif 'Dining' in description or 'Restaurant' in description:
        return 'Food'
    elif 'Uber' in description or 'Taxi' in description:
        return 'Transport'
    elif 'Gas' in description or 'Fuel' in description:
        return 'Transport'
    elif 'Rent' in description:
        return 'Rent'
    elif 'Subscription' in description or 'Netflix' in description or 'Spotify' in description:
        return 'Recurring Subscriptions'
    else:
        return 'Other'

# Group by 'User' and 'Category' to analyze total spending
df['Category'] = df['Description'].apply(categorize_expense)

grouped = df.groupby(['User', 'Category']).agg({'Amount': 'sum'}).reset_index()

# Pivot to compare spending across users
summary = grouped.pivot(index='Category', columns='User', values='Amount').fillna(0)
print(summary)