from transactions import transactions
from expenseCategorization import categorize_transactions
from dataAndAnalytics import calculate_monthly_spending
from monthlyReport import generate_monthly_report
from dataProcessing import calculate_category_percentiles, generate_spending_comparison_report

def main():
    # Step 1: Categorize the transactions
    categorized_transactions = categorize_transactions(transactions)
    
    # Step 2: Calculate monthly spending
    monthly_spending = calculate_monthly_spending(categorized_transactions)
    
    # Step 3: Generate the monthly report
    report = generate_monthly_report(monthly_spending)
    
    # Step 4: Display the report
    print(report)

if __name__ == "__main__":
    main()