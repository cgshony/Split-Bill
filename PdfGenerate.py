from fpdf import FPDF

class PdfReport:
    """
    Creates a PDF file that contains names, due amount. period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add watermark
        # pdf.image('house.png', w=30, h=30)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align="C", ln=1)

        # insert period label and value
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, align="C", ln=1)

        # insert name and due amount first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=1, ln=1)

        # insert name and due amount first flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=1, ln=1)

        pdf.output(self.filename)