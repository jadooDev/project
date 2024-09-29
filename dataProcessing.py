import pandas as pd
import numpy as np
from transactions import transactions, categories

# Create a dataframe from transactions
transactions_df = pd.DataFrame(transactions)

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
    category_spending = transactions_df[transactions_df['Category'] == category]['Amount']
    
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
