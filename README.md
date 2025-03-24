# AUTOMATED-REPORT-GENERATION

company : CODTECH IT SOLUTION

NAME : DIVYANSHI KUSHWAH

*INTERN ID * : CT08WQT

DOMAIL : PYTHON PROGRAMMING

DURATION :4 WEEKS

MENTOR :NEELA SANTHOSH

DESCRIPTION
This Python script is designed to read data from a CSV file and generate a well-structured PDF report using the `pandas` and `fpdf` libraries. The script begins with a function that reads the CSV file into a Pandas DataFrame, ensuring that errors in reading the file are caught and reported. The main functionality for generating the PDF is encapsulated in a custom `PDF` class, which extends the `FPDF` library. This class defines custom header and footer methods, displaying a title at the top of each page and a page number at the bottom. The key feature of the PDF generation is the `add_table()` method, which formats the data into a table with clear borders, headers, and rows, making it easy to read. The table is populated with the data from the CSV, with each column name displayed as the table header and each row’s values printed below. The script coordinates this process in the main block, where it reads the data, creates a PDF document, and outputs the report as a file named `Employee_Report.pdf`. This approach offers a seamless solution for turning CSV data into a professional PDF report, with clear formatting and structured content. The script is flexible and can be adapted to different datasets, though it could be enhanced by dynamically adjusting column widths for larger or more complex datasets.
