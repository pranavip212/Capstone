from estimated_costs import CostEstimator

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
        yearly_income = (
            user.monthly_income * 12
            + osap["grant"]
        )

        # NOTE: loan is NOT income
        #expenses
        yearly_expenses = (
            scenario.tuition
            + housing
            + food
            + transport
        )

        disposable = yearly_income - yearly_expenses

        #allocation
        profile = BudgetGenerator.SPENDING_PROFILES[
            user.spending_style
        ]

        return {
            "income": yearly_income,
            "expenses": yearly_expenses,
            "disposable": disposable,

            "savings": disposable * profile["savings"],
            "leisure": disposable * profile["leisure"],
            "emergency": disposable * profile["emergency"]
        }

