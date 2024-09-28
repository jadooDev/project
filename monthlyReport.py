def generate_monthly_report(monthly_spending):
    report = "----- Your Monthly Spending Report -----\n"
    
    for month, categories in monthly_spending.items():
        report += f"\nMonth: {month}\n"
        for category, amount in categories.items():
            report += f"- {category}: ${amount:.2f}\n"

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