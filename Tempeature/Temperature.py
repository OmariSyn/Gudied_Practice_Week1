from datetime import datetime


def convertData(data):
    
    
    
    return (data - 32) * 5/9  

def getInput():
   
    num_entries = int(input("How many entries are being entered? "))

    
    for i in range(num_entries):
        entry_date = input(f"\nEntry {i+1} - Enter the date: ")
        value = float(input(f"Entry {i+1} - Enter the value (F, lbs, or inches): "))

       
        converted_value = convertData(value)

        
        print(f"The following was saved at {datetime.now()}:")
        print(f"Date: {entry_date}, Original Value: {value}, Converted Value: {converted_value:.2f}")



print('omarijoh0314 Excel SpreadSheet Automation Menu')
print('Choose a number from the Following options')
print("1. Input Data")
print('2. View Current Date')
print('3. Generate Report')

selection = input("\nSelection: ")

# Error-checking code and menu logic
if selection == "1":
    getInput()
else:
    # Else statement for anything other than "1"
    print("Error: The chosen functionality is not implemented yet")