class P_L():
    def __init__(self, income, tax, insurance, electric, water, sewer, garbage, gas, hoa, lawn, vacancy, repairs, capex, management, mortgage):
        self.income = income
        self.expenses = {
            'tax': tax,
            'insurance': insurance,
            'utilities': {
                'electric': electric,
                'water': water,
                'sewer': sewer,
                'garbage': garbage,
                'gas': gas
            },
            'hoa': hoa,
            'lawn': lawn,
            'vacancy': vacancy,
            'repairs': repairs,
            'capex': capex,
            'management': management,
            'mortgage': mortgage
        }



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
        self.rental = rental
        super().__init__(rental, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def monthly_mortgage(self, loan_amount, interest_rate, loan_term):
        rate = (interest_rate/100) / 12
        mortgage = loan_amount * (rate(1 + rate) ** loan_term) / ((1 + rate) ** loan_term - 1)
        return mortgage

    def monthly_cash_flow(self, cash_flow):
        self.expenses['mortgage'] = self.monthly_mortgage()
        cash_flow = self.income - sum(self.expenses.values())
        return cash_flow

    def total_investment(self, total):
        total = self.down_payment - self.closing_costs - self.rehab_budget - self.misc_others
        return total

    def coc_roi(self, roi):
        roi = (self.monthly_cash_flow* 12) / self.total_investment
        return roi

    def run(self):
        while True:
            purchase_price = input('Please enter in the purchase price: ')
            closing_costs = input('Please enter in the estimated closing: ')
            rehab = input('Please enter in the estimated rehab cost: ')
            rental = input('Please enter in the estimated rental income: ')
            loan_amount = input('Please enter in the loan amount: ')
            interest_rate = input('Please enter in the interest rate %: ')
            loan_term = input('Please enter in the loan term (in months): ')
            investment = Formula(purchase_price, 0, loan_amount, interest_rate, loan_term, closing_costs, rehab, 0, rental)
            investment.monthly_mortgage(loan_amount, interest_rate, loan_term)


investment = Formula('purchase_price', 'down_payment', 'loan_amount', 'interest_rate', 'loan_term', 'closing_costs', 'rehab_budget', 'misc_others', 'rental')
investment.run()