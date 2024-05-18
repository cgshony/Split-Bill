from fpdf import FPDF

class PdfReport:
    """
    Creates a PDF file that contains records for  names, due amounts, and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generatePDF(self, flatmates, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Optional: Add watermark
        # pdf.image('sth.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Monthly Bill', border=1, align="C", ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, align="C", ln=1)

        # Insert names and due amounts for each flatmate
        pdf.set_font(family='Times', size=12)
        for flatmate in flatmates:
            pdf.cell(w=100, h=40, txt=flatmate.name, border=1)
            amount_due = round(flatmate.pay_due(bill, flatmates), 2)
            pdf.cell(w=150, h=40, txt=f"£{amount_due}", border=1, ln=1)

        try:
            pdf.output(self.filename)
            print(f"PDF generated successfully: {self.filename}")
        except Exception as e:
            print(f"An error occurred while generating the PDF: {e}")
