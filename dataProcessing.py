
import pandas as pd
import numpy as np
from transactions import transactions, categories

# Create a DataFrame from transactions
transactions_df = pd.DataFrame(transactions)

def calculate_category_percentiles(transactions_df, categories):
    """
    Calculates the percentile ranking of spending in each category based on transaction data.
    
    Returns:
        A dictionary where keys are categories and values are the percentile ranks of spenders in that category.
    """
    percentiles = {}

    for category in categories:
        category_spending = transactions_df[transactions_df['category'] == category]['amount']
        
        if len(category_spending) == 0:
            # If no spending data for this category, default to 0 percentile
            percentiles[category] = 0
        else:
            # Calculate percentiles based on all users' spending in this category
            percentile = np.percentile(category_spending, [25, 50, 75, 90])  # Example percentiles: 25th, 50th, 75th, 90th
            percentiles[category] = {
                '25th': percentile[0],
                '50th': percentile[1],
                '75th': percentile[2],
                '90th': percentile[3],
            }
    
    return percentiles

def rank_user_spending_vs_others(user_spending, transactions_df):
    """
    Ranks user spending versus the rest of the users based on transaction data.
    
    Args:
        user_spending: A dictionary of user spending in each category.
        transactions_df: DataFrame containing all transaction data.
    
    Returns:
        A dictionary where each category maps to the user's percentile rank.
    """
    percentiles = {}

    for category, user_amount in user_spending.items():
        category_spending = transactions_df[transactions_df['category'] == category]['amount']
        
        if len(category_spending) == 0:
            # If no one else spent in this category, assume user is in the top percentile
            percentile_rank = 100 if user_amount > 0 else 0
        else:
            # Calculate the percentile rank based on how many people spent less than the user
            percentile_rank = np.sum(category_spending < user_amount) / len(category_spending) * 100
        
        percentiles[category] = percentile_rank
    
    return percentiles

def generate_spending_comparison_report(user_spending, transactions_df, categories):
    """
    Generates a report comparing user spending to percentile ranks of other spenders.
    
    Args:
        user_spending: Dictionary of user spending in each category.
        transactions_df: DataFrame containing transaction data.
        categories: Dictionary of spending categories.
    
    Returns:
        A string report with insights.
    """
    report = "User Spending vs. Others Report\n\n"
    percentile_ranks = rank_user_spending_vs_others(user_spending, transactions_df)

    for category in categories:
        user_amount = user_spending.get(category, 0)
        report += f"\nIn the {category} category:\n"
        report += f" - You spent: ${user_amount:.2f}\n"
        
        if category in percentile_ranks:
            percentile_rank = percentile_ranks[category]
            if percentile_rank >= 90:
                report += f" - You are in the top {100 - percentile_rank:.2f}% of spenders (spending more than {percentile_rank:.2f}% of users).\n"
            elif percentile_rank >= 50:
                report += f" - You spend more than {percentile_rank:.2f}% of users.\n"
            else:
                report += f" - You spend less than {100 - percentile_rank:.2f}% of users.\n"
        else:
            report += " - No data available for this category.\n"

    return report