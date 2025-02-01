import streamlit as st
from calc import calculate_tax

def main():
    st.title("Income Tax Calculator")

    income = st.number_input("Enter your annual income (in ₹):", min_value=0.0, format="%.2f")
    nps_percentage = st.number_input("Enter NPS investment (in %):", min_value=0.0, max_value=100.0, format="%.2f")
    basic_salary_percentage = st.number_input("Enter Basic Salary percentage (in %):", min_value=0.0, max_value=100.0, format="%.2f")

    if st.button("Calculate Tax"):
        tax, nps_investment, taxable_income = calculate_tax(income, nps_percentage, basic_salary_percentage)

        st.write(f"Your NPS investment: ₹{nps_investment:,.2f}")
        st.write(f"Your taxable income after deductions: ₹{taxable_income:,.2f}")
        st.write(f"Your total income tax payable: ₹{tax:,.2f}")

if __name__ == "__main__":
    main()