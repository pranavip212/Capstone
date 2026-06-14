class UserProfile:
    def __init__(self, monthly_income, current_savings, scholarship_amount, family_support, spending_style, osap_level):

        self.monthly_income = monthly_income
        self.current_savings = current_savings
        #consider moving scholarships to uni tab, can change or given by school
        self.scholarship_amount = scholarship_amount
        self.monthly_family_support = family_support
        self.spending_style = spending_style # 1-5, frugal to social, maybe a slider on the gui?
        self.osap_level = osap_level # none, low, avg, high (grants & loans spilt up based on this, estimated amount can be overwritten)

