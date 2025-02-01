def calculate_tax(income, nps_percentage, basic_salary_percentage):
    # Calculate NPS investment
    nps_investment = income * (nps_percentage / 100)

    # Calculate taxable income
    taxable_income = income - nps_investment

    # Define tax slabs and rates
    tax_slabs = [
        (250000, 0.05),
        (500000, 0.1),
        (750000, 0.15),
        (1000000, 0.2),
        (1250000, 0.25),
        (float('inf'), 0.3)
    ]

    tax = 0
    prev_limit = 0

    for limit, rate in tax_slabs:
        if taxable_income > prev_limit:
            taxable_amount = min(taxable_income, limit) - prev_limit
            tax += taxable_amount * rate
            prev_limit = limit
        else:
            break

    # Apply rebate under Section 87A if taxable income ≤ ₹12,75,000
    if taxable_income <= 1275000:
        tax = 0  

    # Apply Health and Education Cess (4% of tax)
    cess = tax * 0.04
    total_tax = tax + cess

    return total_tax, nps_investment, taxable_income