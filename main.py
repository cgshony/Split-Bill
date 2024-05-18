from PdfGenerate import PdfReport
from utilities import Bill, Flatmate


def get_bill_information():
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
    amount, period = get_bill_information()
    flatmates = []

    num_flatmates = int(input(f'How many flatmates are in the flat? '))

    for person in range(num_flatmates):
        flatmate = get_flatmate_details(person)
        flatmates.append(flatmate)

    bill_total = Bill(amount, period)

    # Calculate and print each flatmate's share
    for flatmate in flatmates:
        amount_due = round(flatmate.pay_due(bill_total, flatmates), 2)
        print(f'{flatmate.name} pays: ', amount_due)

  # Generate PDF report
    pdf_report = PdfReport(filename=f'{bill_total.period}.pdf')
    pdf_report.generatePDF(flatmates, bill_total)


if __name__ == "__main__":
    main()


