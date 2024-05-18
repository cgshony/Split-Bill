class Bill:
    """
    Object that contains data about a bill , such as total amount and period of the bill """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a bill  """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pay_due(self, bill, all_flatmates):
        """
        Calculates how much a given flatmate owes for a bill
        based on the number of days they stayed in the house. """

        total_days = 0
        for flatmate in all_flatmates:
            total_days += flatmate.days_in_house

        # Calculate portion of the bill this flatmate has to pay.
        weight = self.days_in_house / total_days
        to_pay = bill.amount * weight

        return to_pay
