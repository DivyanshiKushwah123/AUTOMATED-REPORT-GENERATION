import pandas as pd
from fpdf import FPDF

# Function to Read Data from CSV File
def read_data(file):
    try:
        df = pd.read_csv(file)
        print("Data Read Successfully!")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error Reading File: {e}")
        return None

# Function to Generate PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Data Analysis Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_table(self, df):
        self.set_font("Arial", "", 12)
        self.cell(200, 10, "Employee Data", ln=True, align="L")
        self.ln(5)

        # Table Header
        self.set_fill_color(200, 200, 200)
        for column in df.columns:
            self.cell(40, 10, column, border=1, fill=True)
        self.ln()

        # Table Rows
        for index, row in df.iterrows():
            for column in df.columns:
                self.cell(40, 10, str(row[column]), border=1)
            self.ln()

# Main Function
if __name__ == "_main_":
    file = "data.csv"
    df = read_data(file)

    if df is not None:
        pdf = PDF()
        pdf.add_page()
        pdf.add_table(df)
        pdf.output("Employee_Report.pdf")
        print("PDF Report Generated Successfully!")
