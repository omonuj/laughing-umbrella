def compute_tax(status, income):
    # Define the tax brackets and rates
    brackets = [
        [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],
        [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
    ]
    
    tax_bracket = brackets[status]
    tax = 0.0
    previous_bracket_limit = 0
    
    for limit, rate in tax_bracket:
        if income > limit:
            tax += (limit - previous_bracket_limit) * rate
            previous_bracket_limit = limit
        else:
            tax += (income - previous_bracket_limit) * rate
            break

    return tax

def main():
    print("Enter the filing status:")
    print("0 - Single filers")
    print("1 - Married filing jointly")
    print("2 - Married filing separately")
    print("3 - Head of household")
    
    status = int(input("Status: "))
    income = float(input("Enter the taxable income: "))
    
    tax = compute_tax(status, income)
    print(f"The tax is: ${tax:.2f}")

if __name__ == "__main__":
    main()
