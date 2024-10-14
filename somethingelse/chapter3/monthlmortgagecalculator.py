import math

def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly mortgage payment using the formula:
    M = P[r(1+r)^n] / [(1+r)^n – 1]
    where:
    M = monthly mortgage payment
    P = principal loan amount
    r = monthly interest rate
    n = number of payments (loan term in months)
    """
   
    monthly_interest_rate = annual_interest_rate / 100 / 12
    

    number_of_payments = years * 12
    
    if monthly_interest_rate == 0:
       
        monthly_payment = principal / number_of_payments
    else:
        monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / \
                          ((1 + monthly_interest_rate) ** number_of_payments - 1)
    
    return monthly_payment

def main():
    print("Welcome to the Mortgage Calculator!")
   
    principal = float(input("Enter the loan amount (principal): "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term (in years): "))
   
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
   
    print(f"\nFor a loan amount of ${principal:,.2f} at an annual interest rate of {annual_interest_rate}% over {years} years:")
    print(f"Your monthly mortgage payment will be: ${monthly_payment:,.2f}")

if __name__ == "__main__":
    main()
