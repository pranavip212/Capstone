class CostEstimator:
    #living costs
    @staticmethod
    def estimate_housing(living_situation: str) -> float:
        costs = {
            "home": 0,
            "residence": 12000,
            "apartment": 16800
        }
        return costs.get(living_situation, 0)

    #cost of gas/bus/transportation
    @staticmethod
    def estimate_transportation(commute_type: str, distance_km: float, days_per_week: int):

        if commute_type == "drive":
            annual_km = distance_km * 2 * days_per_week * 30

            fuel_cost = (annual_km / 100) * 8 * 1.50
            return round(fuel_cost)

        elif commute_type == "transit":
            return 120 * 12

        elif commute_type == "walk":
            return 0

        return 0

    #food

    @staticmethod
    def estimate_food(food_level: str) -> float:
        costs = {
            "low": 250,
            "medium": 450,
            "high": 700
        }
        return costs.get(food_level, 450) * 12



    @staticmethod
    def estimate_osap( level: str):
        profiles = {
            "none": {"grant": 0, "loan": 0},
            "average": {"grant": 3000, "loan": 7000},
            "high": {"grant": 5000, "loan": 9000}
        }

        return profiles.get(level, {"grant": 0, "loan": 0})
