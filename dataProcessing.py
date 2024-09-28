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

# Loop through each category and compare the user's spending with others
print("\nRanking of your spending vs the rest of the users:")
for category in categories:
    # Get spending data for the category
    category_spending = df[df['Category'] == category]['Amount']
    
    # Calculate the user's rank based on percentile
    user_amount = user_spending[category]
    percentile_rank = np.sum(category_spending < user_amount) / len(category_spending) * 100
    
    # Display the result
    print(f"\nIn the {category} category:")
    if percentile_rank >= 90:
        print(f"You are in the top {100 - percentile_rank:.2f}% of spenders (spending more than {percentile_rank:.2f}% of users).")
    elif percentile_rank >= 50:
        print(f"You spend more than {percentile_rank:.2f}% of users.")
    else:
        print(f"You spend less than {100 - percentile_rank:.2f}% of users.")

# Example output logic continues here...
