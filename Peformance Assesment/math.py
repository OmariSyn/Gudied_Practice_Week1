

Name = input("Please Enter Your Name: ")
Student_ID = input("Please Enter Your StudentID: ")

number1 = float(input('PLease Enter a whole number: '))

number2 = float(input("Please Enter a diffrent second whole number: "))


answer = number1 * number2

answer2 = number1 / number2

answer3 = number1 + number2


print(f"The Results of {number1} times {number2} is:  {answer:,.2f}")
print(f"The Results of {number1} divide by {number2} is: {answer2:,.2f}")

print(f" The Results of {number1} Plus {number2} is: {answer3:,.2f}")



if number1 > number2:
    print(f" Number1 is Larger than Number 2")
else:
    print("Number2 Is Larger")

print(Name)
print(Student_ID)
