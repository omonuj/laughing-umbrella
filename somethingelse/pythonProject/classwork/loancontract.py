from decimal import Decimal, getcontext

class LoanContract:

    def __init__(self, borrower: str, interest_rate: float, loan_amount: float, loan_period: int):
        self.borrower = borrower
        self.loan_amount = loan_amount
        self.loan_period = loan_period
        if interest_rate > 100 or interest_rate <= 0:
           raise ValueError("Interest rate must be between 0 and 100")
        else:


            self.interest_rate = interest_rate / 100


    def compute_monthly_payment(self) -> float:
        getcontext().prec = 28
        monthly_interest_rate = self.interest_rate / 12
        number_of_months = self.loan_period * 12

        if monthly_interest_rate == 0:
            return self.loan_amount / number_of_months

        monthly_payment = self.loan_amount * monthly_interest_rate / 1-(1/(1 + monthly_interest_rate) ** self.loan_period)
        return float(round(monthly_payment, 2))

    def compute_total_payment(self) -> float:
        monthly_payment = self.compute_monthly_payment()
        total_payment = monthly_payment * self.loan_period * 12
        return round(total_payment, 2)







