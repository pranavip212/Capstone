class BudgetAnalyzer:

    @staticmethod
    def calculate_score(budget):

        score = 0

        # Savings score is out of 25

        if budget['yearly_income'] > 0:
            savings_rate = (budget["savings"] / budget["yearly_income"])
        else:
            savings_rate = 0

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

        if budget['yearly_expenses'] > 0:
            emergency_ratio = budget["emergency"] / budget["yearly_expenses"]
        else:
            emergency_ratio = 0
        score += min(25, emergency_ratio * 100)

        # Debt risk score (/25)

        if budget["disposable"] < 0:
            score += 0

        elif budget["disposable"] < 2000:
            score += 10

        else:
            score += 25

        #score adjustment based on finicial position after using osap loans
        if budget["net_position"] < 0 and budget["net_position_with_loan"] >= 0:
            score += 10


        score = max(0, min(score, 100))
        return round(score)

    @staticmethod
    def generate_recommendations(budget):

        recommendations = []

        if budget["disposable"] < 0:
            recommendations.append("Your expenses exceed your income. Consider reducing housing or transportation costs if possible.")

        if budget["savings"] < 1000:
            recommendations.append(
                "Your yearly savings are low. Consider increasing savings contributions."
                "This will contribute to a higher savings score and total financial score")

        if budget["leisure"] > budget["savings"]:
            recommendations.append("Reducing leisure spending could improve long-term financial stability.")

        if budget["emergency"] < 500:
            recommendations.append("Consider building a larger emergency fund. This will better your financial score as you will be prepared for life's unexpected events")

        if budget["net_position"] < 0:
            recommendations.append("Your available funds do not cover projected expenses.")

        if budget["net_position"] < 0 and budget["net_position_with_loan"] >= 0:
            recommendations.append("Your plan is affordable only with OSAP loans. Consider the long-term impact of borrowing.")

        if budget["osap_loan"] >= 10000:
            recommendations.append("Your projected OSAP loan is substantial. Consider future repayment obligations when choosing a program.")

        if not recommendations:
            recommendations.append("Your budget appears financially stable.")

        return recommendations

    @staticmethod
    def financial_rating(score):
        if score >= 85:
            return "Excellent"

        elif score >= 70:
            return "Good"

        elif score >= 50:
            return "Fair"

        else:
            return "Poor"




