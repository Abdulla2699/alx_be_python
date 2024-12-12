monthly_income = int(input("Enter your monthly income : "))
monthly_expenses = int(input("Enter your total monthly expenses : "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
annula_interest_rate = int(0.05)
projected_savings = annual_savings + annual_savings * 0.05
print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is: {projected_savings}")