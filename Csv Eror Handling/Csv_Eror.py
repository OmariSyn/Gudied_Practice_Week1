import csv
from datetime import datetime

def insertData(path, data_string):
    try:
        # 'a+' opens for appending; creates the file if it doesn't exist
        with open(path, 'a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(data_string.split(','))
            print(f"Saved at {datetime.now().strftime('%H:%M:%S')}: {data_string}")
    except Exception as e:
        print(f"Write Error: {e}")

def viewData(path):
    print(f"\nPath: {path}")
    try:
        # 'r' is the minimal permission for reading
        with open(path, 'r', encoding='utf-8') as f:
            for row in csv.reader(f): print(", ".join(row))
    except Exception as e:
        print(f"Read Error: {e}")

def getInput():
    try:
        # Collecting previous week's style input
        val = input("Enter Animal, Species, Age (comma-separated): ")
        insertData("ZooData.csv", val)
    except Exception as e:
        print(f"Input Error: {e}")

# Main Menu Flow
while True:
    choice = input("\n1: Add Data, 2: View Data, 3: Exit: ")
    if choice == "1": 
        getInput()
    elif choice == "2": 
        viewData("ZooData.csv")
    elif choice == "3": 
        break