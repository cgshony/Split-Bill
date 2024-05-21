"""
Main module for the Flatmates Split Bill application.

This script handles user interaction, retrieves bill and flatmates count information,
stores data to a SQL database, returns the amount due for each flatmate,
and generates a PDF report as a receipt.
"""

from PdfGenerate import PdfReport
from utilities import Bill, Flatmate
from SQLdatabase import create_database, create_tables, connect_to_database
from email_send import send_email
import mysql.connector

def get_bill_information():
    #Receive information from the user about the bill amount and period.

    while True:
        try:
            amount = float(input('Hello! Please enter the bill amount: '))
            period = input('Please enter the bill period? (E.g May, 2024) ')
            return amount, period
        except ValueError:
            print("Invalid input. Please enter the values again.")

def get_flatmate_details(id):
    name = input(f"What is the name of flatmate {id + 1}? ")
    days_in_house = int(input(f'How may days did {name} stay in the house during this period '))
    return Flatmate(name, days_in_house)

def main():
    """
       The main function creates the database and tables, retrieves user inputs,
       stores data to the database, calculates the amount due for each flatmate,
       and generates a PDF report.
       """

    #Create  database and tables
    create_database()
    create_tables()

    # Connect to the database
    db = connect_to_database()
    cursor = db.cursor()

    #retreive information about the monthly bill
    amount, period = get_bill_information()
    flatmates = []

    num_flatmates = int(input(f'How many flatmates are in the flat? '))

    for person in range(num_flatmates):
        flatmate = get_flatmate_details(person)
        flatmates.append(flatmate)

    # List of emails for each flatmate to automatically send them the monthly bill
    emails = [
        'shony.alexandrova@gmail.com'
        #'flatmate2@example.com',
        #'flatmate3@example.com'
    ]

    bill_total = Bill(amount, period)
    bill_id = bill_total.save(cursor) #save to db
    db.commit()

    # Save each flatmate to the database
    for flatmate in flatmates:
        flatmate.save(cursor, bill_id)
    db.commit()

    # Calculate and print each flatmate's share
    for flatmate in flatmates:
        amount_due = round(flatmate.pay_due(bill_total, flatmates), 2)
        print(f'{flatmate.name} pays: ', amount_due)


    # Generate PDF report
    pdf_report = PdfReport(filename=f'{bill_total.period}.pdf')
    pdf_report.generatePDF(flatmates, bill_total)

    #Send an automated email with the generated monthly bill
    from_email = 'shony.alexandrova@gmail.com'

    for flatmate, email in zip(flatmates, emails):
        subject = "Your Monthly Bill"
        body = f"Hello {flatmate.name},\n\nPlease find attached your bill for the period {bill_total.period}.\n\nBest regards,\nYour Flatmates Bill App"
        send_email(from_email, email, subject, body, pdf_report.filename)
        print('Email was sent to flatmates!')

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
