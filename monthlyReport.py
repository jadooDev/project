def generate_monthly_report(monthly_spending): 
    report = "Your Monthly Spending Report\n" # Header for report
    
    for month, categories in monthly_spending.items(): #loop to iterate over monthly spending returning month and category
        report += f"\nMonth: {month}\n" #append the current month to the report string
        for category, amount in categories.items(): # this loop goes through each category and returns amount spent in that month
            report += f" {category}: ${amount:.2f}\n" # appends category and amount spent to string retun

    report += "\n\nOverall Insights:\n"
    insights = generate_insights(monthly_spending)
    for insight in insights:
        report += f"{insight}\n"
    
    return report

# Categorize, calculate spending, and generate report
categorized_transactions = categorize_transactions(transactions)
monthly_spending = calculate_monthly_spending(categorized_transactions)
report = generate_monthly_report(monthly_spending)
print(report)