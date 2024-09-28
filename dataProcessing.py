import pandas as pd
import numpy as np

# Sample data for multiple users (excluding current user data)
users = [f'User_{i}' for i in range(1, 21)]  # User_1 to User_20
categories = ['Food', 'Transport', 'Rent', 'Recurring Subscriptions', 'Health']
dates = pd.date_range(start='2024-09-01', periods=30, freq='D')

# Create a DataFrame with random spending data for each user
np.random.seed(42)

data = {
    'Date': np.random.choice(dates, 100),
    'User': np.random.choice(users, 100),
    'Category': np.random.choice(categories, 100),
    'Amount': np.random.randint(10, 1000, size=100)
}

df = pd.DataFrame(data)

# Group the other users' data by Category and calculate the average spending
average_spending = df.groupby('Category')['Amount'].mean()

# Display the average spending for other users
print("Average spending of other users by category:")
print(average_spending)

# Function to get the user's spending input
def get_user_spending(categories):
    user_spending = {}
    print("\nEnter your spending for each category:")
    for category in categories:
        amount = float(input(f"{category}: "))
        user_spending[category] = amount
    return user_spending

# Get user spending input
user_spending = get_user_spending(categories)

# Convert user spending into a DataFrame for comparison
user_df = pd.DataFrame(list(user_spending.items()), columns=['Category', 'Amount'])

# Merge user spending with the average spending for comparison
comparison_df = user_df.merge(average_spending.reset_index(), on='Category', suffixes=('_User', '_Average'))

# Calculate the percentage difference between user spending and the average
comparison_df['Percentage_Difference'] = ((comparison_df['Amount_User'] - comparison_df['Amount_Average']) / comparison_df['Amount_Average']) * 100

# Display the comparison
print("\nComparison of your spending vs average spending by other users:")
print(comparison_df[['Category', 'Amount_User', 'Amount_Average', 'Percentage_Difference']])

# Provide insights on whether the user's spending is higher or lower
for _, row in comparison_df.iterrows():
    if row['Percentage_Difference'] > 0:
        print(f"\nYou are spending {row['Percentage_Difference']:.2f}% more than the average user on {row['Category']}.")
    else:
        print(f"\nYou are spending {-row['Percentage_Difference']:.2f}% less than the average user on {row['Category']}.")
