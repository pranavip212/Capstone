class BudgetAnalyzer:

    @staticmethod
    def calculate_score(budget):

        score = 0

        # Savings score is out of 25

        savings_rate = budget["savings"] / budget["income"]

        score += min(25, savings_rate * 50)

        # Disposable income score out of 25

        if budget["disposable"] > 5000:
            score += 25

        elif budget["disposable"] > 2500:
            score += 18

        elif budget["disposable"] > 1500:
            score += 14

        elif budget["disposable"] > 1000:
            score += 10

        elif budget["disposable"] > 0:
            score += 5

        # Emergency fund score (/25)

        emergency_ratio = (budget["emergency"] /budget["expenses"])

        score += min(25, emergency_ratio * 100)

        # Debt risk score (/25)

        if budget["disposable"] < 0:
            score += 0

        elif budget["disposable"] < 2000:
            score += 10

        else:
            score += 25

        return round(min(score, 100))

    @staticmethod
    def generate_recommendations(budget):

        recommendations = []

        if budget["disposable"] < 0:
            recommendations.append(
                "Your expenses exceed your income. Consider reducing housing or transportation costs if possible."
            )

        if budget["savings"] < 1000:
            recommendations.append(
                "Your yearly savings are low. Consider increasing savings contributions."
                "This will contribute to a higher savings score and total financial score"
            )

        if budget["leisure"] > budget["savings"]:
            recommendations.append(
                "Reducing leisure spending could improve long-term financial stability."
            )

        if budget["emergency"] < 500:
            recommendations.append(
                "Consider building a larger emergency fund. This will better your financial score as you will be prepared for life's unexpected events"
            )

        if not recommendations:
            recommendations.append(
                "Your budget appears financially stable."
            )

        return recommendations