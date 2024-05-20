"""
Utilities module for the Flatmates Split Bill application.

This module contains the Bill and Flatmate classes, representing a monthly
bill and a flatmate in the household, and provide methods to interact
with the database.
"""

import mysql.connector

class Bill:
    """ A class that contains data about a bill , such as total amount and period of the bill """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    def save(self, cursor):
        """Save the bill to the database. """

        cursor.execute("INSERT INTO bills (amount, period) VALUES (%s, %s)", (self.amount, self.period))
        return cursor.lastrowid


class Flatmate:
    """ Create a flatmate representative who lives in the flat and pays portion of the monthly bill.  """

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

    def save(self, cursor, bill_id):
        """ Save the flatmate information to the database."""

        cursor.execute("INSERT INTO flatmates (name, days_in_house, bill_id) VALUES (%s, %s, %s)",
                       (self.name, self.days_in_house, bill_id))
        return cursor.lastrowid
