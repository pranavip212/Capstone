from estimated_costs import CostEstimator
from user_profile import UserProfile

class BudgetGenerator:
    #money allocation based on user profile/preference
    SPENDING_PROFILES = {
        1: {"savings": 0.70, "leisure": 0.20, "emergency": 0.10},
        2: {"savings": 0.55, "leisure": 0.25, "emergency": 0.20},
        3: {"savings": 0.40, "leisure": 0.40, "emergency": 0.20},
        4: {"savings": 0.30, "leisure": 0.55, "emergency": 0.15},
        5: {"savings": 0.20, "leisure": 0.70, "emergency": 0.10},
    }

    @staticmethod
    def generate_budget(user, scenario):
        #autofill using estimated costs
        housing = CostEstimator.estimate_housing(
            scenario.living_situation
        )

        food = CostEstimator.estimate_food(
            scenario.food_level
        )

        transport = CostEstimator.estimate_transportation(
            scenario.commute_type,
            scenario.commute_distance,
            scenario.days_on_campus
        )

        osap = CostEstimator.estimate_osap(
            user.osap_level
        )

        # income
        yearly_income = (user.monthly_income * 12 + osap["grant"] + user.monthly_family_support *12 + user.scholarship_amount)
        total_available_funds = (user.current_savings + yearly_income)

        # NOTE: loan is NOT income
        #expenses
        yearly_expenses = (scenario.tuition + housing + food + transport)

        disposable = yearly_income - yearly_expenses

        #allocation
        profile = BudgetGenerator.SPENDING_PROFILES[user.spending_style]

        if disposable > 0:
            savings = disposable * profile["savings"]
            leisure = disposable * profile["leisure"]
            emergency = disposable * profile["emergency"]
        else:
            savings = 0
            leisure = 0
            emergency = 0

        net_position = total_available_funds - yearly_expenses

        available_with_loan = total_available_funds + osap["loan"]

        net_position_with_loan = available_with_loan - yearly_expenses


        return {
            #user factors
            "employment_income": user.monthly_income * 12,
            "family_support": user.monthly_family_support,
            "scholarship_amount": user.scholarship_amount,
            "osap_grant" : osap["grant"],
            "osap_loan": osap['loan'],

            "yearly_income": yearly_income,
            "current_savings": user.current_savings,
            "total_available_funds": total_available_funds,
            "available_with_loan": available_with_loan,

            #all the expenses
            "tuition": scenario.tuition,
            "housing": housing,
            "food": food,
            "transportation": transport,
            "yearly_expenses": yearly_expenses,

            #budget
            "disposable":  disposable,
            "savings": savings,
            "leisure": leisure,
            "emergency": emergency,

            # monthly numbers
            "monthly_income": yearly_income / 12,
            "monthly_expenses": yearly_expenses / 12,
            "monthly_disposable": disposable / 12,
            "monthly_savings": (disposable * profile["savings"]) / 12,
            "monthly_leisure": (disposable * profile["leisure"]) / 12,
            "monthly_emergency": (disposable * profile["emergency"]) / 12,

            "net_position": net_position,
            "net_position_with_loan": net_position_with_loan



        }


