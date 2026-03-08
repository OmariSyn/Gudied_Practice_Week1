from datetime import datetime


print('omarijoh0314 Excel SpreadSheet Automation Menu')
'Choose a number from the Following  options'

print("1. Input Data")
print('2 View Current Date' )
print('3 Generate Report')


choice = input("Enter a Choice Please: ")

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
now = datetime.now()
current_date = now.date()

if choice  == '1':
    print(f"You have Selected 1 at {time}")
elif choice == '2':
    print(f"The time and date is: {current_date}") 
elif choice == '3':
   print(f"Generating Report Now At: {time}" )

