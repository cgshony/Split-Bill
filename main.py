from PdfGenerate import PdfReport
from  utilities import Bill, Flatmate


amount = float(input('Hello! Please enter the bill amount: '))
period = input('Whet is the bill period? E.g May 2024')

name1 = input('What is your name? ')
days_in_house1 = int(input(f'How may days did {name1} stay in the house during this period'))

name2 = input('What is the name of the other flatmate? ')
days_in_house2 = int(input(f'How may days did {name1} stay in the house during this period'))

bill_total = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f'{name1} pays: ', flatmate1.pays(bill_total, flatmate2))
print(f'{name2} pays: ', flatmate2.pays(bill_total, flatmate1))

pdf_report = PdfReport(filename=f'{bill_total.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, bill_total)