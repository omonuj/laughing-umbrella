import unittest

import pytest

from pythonProject.classwork.loancontract import LoanContract


class MyTestCase(unittest.TestCase):

    #def setUp(self):
        #loan_contract = LoanContract(borrower="john odoh", interest_rate = 12, loan_amount= 4_300_000.0, loan_period = 1)


    def test_LoanContract_can_calculate_monthly_payment(self):
        loan_contract = LoanContract(borrower="john odoh", interest_rate = 12, loan_amount= 4_400_500.0, loan_period = 1)
        monthly_payment = loan_contract.compute_monthly_payment()
        assert monthly_payment == pytest.approx(44000.01, 0.01)


    def test_that_can_calculate_total_payment(self):
        loan_contract = LoanContract(borrower="john odoh", interest_rate = 12, loan_amount= 10000, loan_period = 1)

        total_payment = loan_contract.compute_total_payment()
        assert total_payment == pytest.approx(1188.12, 0.01)

    def test_LoanContract_invalid_interest_rate(self):
        with pytest.raises(ValueError, match="Interest rate must be between 0 and 100"):
            LoanContract("john doe", 0, 10000, 5)

    def test_interest_rate_cannot_go_above_100(self):
       with pytest.raises(ValueError, match="Interest rate must be between 0 and 100"):
               LoanContract("john doe", 102, 10000, 5)

    def test_total_loan_repayment(self):
        loan_contract = LoanContract(borrower="john odoh", interest_rate = 12, loan_amount= 4_300_000.0, loan_period = 1)

        total_payment = loan_contract.compute_total_payment()
        assert total_payment == pytest.approx(515988.12, 0.01)






if __name__ == '__main__':
    unittest.main()
