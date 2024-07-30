#program that calcuates interest rate 

#defines method
def calculate_initial_savings(final_amount, interest_rate, years):

#innitializes inerest rate formula and converts to percentage
    interest_rate = interest_rate / 100  

    initial_savings = final_amount / (1 + interest_rate) ** years
    return initial_savings

final_amount = 5000
interest_rate = 25
years = 3

initial_savings = calculate_initial_savings(final_amount, interest_rate, years)
print(f"You need to save approximately ${initial_savings:.2f} initially.")
