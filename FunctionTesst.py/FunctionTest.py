def functionOne():
     StudnetName = print("My StudentID is omarijoh0314")
     return StudnetName
   


def functionTwo():
     number1 = int(input("Enter a Number: "))
     number2 = int(input("Enter another Number: "))
     total = number1 + number2
     print(f"the Sum of {number1} and {number2} is {total}")
     return total


def FunctionThree(passed_sum):
     if passed_sum >5:
          print(f"The Sum is Greater then 5")
     elif passed_sum <5:
          print(f"The Sum is less then 5")
     print("FunctionThree Return 0314")
     
     



def main():
     functionOne()
     the_Results =  functionTwo()
     FunctionThree(the_Results)
main()


     
     




