import csv
from datetime import datetime
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference

# Function: createChart
# Args: path (str), c_type (str) | Returns: None
def createChart(path, c_type):
    # Ask for data source and map to column index (1 for initial, 2 for converted)
    src = input("Source: 1 (Initial) or 2 (Converted): ")
    idx = 1 if src == "1" else 2
    
    # Extract data from CSV
    dates, values = [], []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        for r in reader:
            dates.append(r[0])
            values.append(float(r[idx]))

    # Setup Excel and Write Data
    wb = Workbook()
    ws = wb.active
    ws.append(["Date", "Value"])
    for d, v in zip(dates, values):
        ws.append([d, v])

    # Build Chart (Bar or Line)
    chart = BarChart() if c_type == "bar" else LineChart()
    data = Reference(ws, min_col=2, min_row=1, max_row=len(values)+1)
    cats = Reference(ws, min_col=1, min_row=2, max_row=len(values)+1)
    
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    chart.x_axis.title, chart.y_axis.title = "Date", "Value"
    chart.title = f"student1234 {datetime.now().strftime('%m/%d/%Y')}"

    ws.add_chart(chart, "E2")
    wb.save("final.xlsx")
    print("Report Saved to final.xlsx")

# Function: generateReport
# Args: path (str) | Returns: None
def generateReport(path):
    chart_type = input("Enter chart type (line/bar): ").lower()
    createChart(path, chart_type)