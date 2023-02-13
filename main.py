class P_L():
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = {}



class Formula(P_L):
    def __init__(self, purchase_price, down_payment, loan_amount, interest_rate, loan_term, closing_costs, rehab_budget, misc_others, rental):
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_others = misc_others
        super().__init__(rental, 0)

    def monthly_mortgage(self, loan_amount, interest_rate, loan_term):
        payments = Formula(0, 0, loan_amount, interest_rate, loan_term, 0, 0, 0, 0)
        monthly_rate = (interest_rate/100) / 12
        mortgage = loan_amount * (monthly_rate * (1 + monthly_rate) ** loan_term) / ((1 + monthly_rate) ** loan_term - 1)
        print(f'Your monthly principle and interest payment will be ${round(mortgage, 2)}.')
        return 

    def monthly_cash_flow(self):
        cash_flow = self.income - sum(self.expenses.values())
        print(f'Your estimated monthly cashflow will be ${cash_flow}.')
        return 

    def total_investment(self, down_payment, closing_costs, rehab_budget, misc_others):
        payments = Formula(0, down_payment, 0, 0, 0, closing_costs, rehab_budget, misc_others, 0)
        total = down_payment + closing_costs + rehab_budget + misc_others
        print(f'Your total estimated investment is ${round(total, 2)}.')

    def coc_roi(self, roi):
        roi = (self.monthly_cash_flow* 12) / self.total_investment
        return roi

    def run(self):
            loan_amount = int(input('Please enter in the loan amount: '))
            interest_rate = int(input('Please enter in the interest rate %: '))
            loan_term = int(input('Please enter in the loan term (in months): '))
            self.monthly_mortgage(loan_amount, interest_rate, loan_term)
            down_payment = int(input('Please enter in the amount of down payment: '))
            closing_costs = int(input('Please enter in the estimated closing costs: '))
            rehab = int(input('Please enter in the estimated rehab costs: '))
            misc_others = int(input('Please enter in any other misc costs: '))
            self.total_investment(down_payment, closing_costs, rehab, misc_others)
            rental = int(input('Please enter in the estimated rental income: '))
            tax = int(input('Please enter in the estimated property tax: '))
            insurance = int(input('Please enter in the estimated property insurance: '))
            self.income = rental
            self.expenses = {'tax': tax, 'insurance': insurance}
            self.monthly_cash_flow()
#         except:
#             print('Please enter the amount in digits without any expressions')
            
investment = Formula('', '', '', '', '', '', '', '', '') 
investment.run()
