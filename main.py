from user_profile import UserProfile
from university_expenses import UniversityExpenses
from budget import BudgetGenerator


def main():

    # -------------------------
    # CREATE USER
    # -------------------------
    user = UserProfile(
        monthly_income = 1200,
        current_savings = 5000,
        spending_style = 3,
        osap_level = "average",
        scholarship_amount = 0,
        family_support= 0


    )

    # -------------------------
    # CREATE SCENARIO
    # -------------------------
    scenario = UniversityExpenses(
        university_name="Ontario Tech",
        program_name="Mechatronics Engineering",
        tuition=9800,
        living_situation="home",
        commute_type="drive",
        commute_distance=15,
        days_on_campus=5,
        food_level="medium"
    )

    # -------------------------
    # GENERATE BUDGET
    # -------------------------
    budget = BudgetGenerator.generate_budget(user, scenario)

    # -------------------------
    # OUTPUT
    # -------------------------
    print("\n=== BUDGET REPORT ===")
    print(f"Income: ${budget['income']}")
    print(f"Expenses: ${budget['expenses']}")
    print(f"Disposable: ${budget['disposable']}")
    print(f"Savings: ${budget['savings']}")
    print(f"Leisure: ${budget['leisure']}")
    print(f"Emergency: ${budget['emergency']}")


if __name__ == "__main__":
    main()