# Flatmates Split-Bill Application

This Python application calculates and splits monthly bills among flatmates, saves the data to a MySQL database, generates a PDF report outlining each flatmate's share, and sends the report via an automated email.

## Features:
- Calculate the amount each flatmate owes based on their stay duration during a monthly billing period.
- Store bill and flatmate data in a MySQL database.
- Generate a PDF report with the billing details.
- Automatically send the PDF report to each flatmate via email.

## Project Structure
- `main.py`: The main script that handles user interactions, retrieves bill and flatmate information, stores data in the database, calculates each flatmate's share, generates a PDF report, and sends it via email.
- `utilities.py`: Contains the `Bill` and `Flatmate` classes, with methods to calculate dues and save data to the database.
- `PdfGenerate.py`: Contains the `PdfReport` class to generate a PDF report with the billing details.
- `SQLdatabase.py`: Handles the creation and connection of the MySQL database and tables.

## Contributing
Contributions are welcome! Please create an issue or pull request with your suggestions or improvements.


## Acknowledgments
- fpdf2 (https://pypi.org/project/fpdf2/) for PDF generation
- mysql-connector-python - (https://pypi.org/project/mysql-connector-python/) for MySQL database connectivity
- freeCodeCamp](https://www.freecodecamp.org/news/how-to-build-an-automated-email-system-with-python/ for the email automation guide
