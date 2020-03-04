
#Calculator Perform
print("Choose your Action (1.Add,2.Subtraction,3.Multiplication,4.Division)")
inp=input("Enter your action :")
print("You selected to perform :",inp)
firstNumber=input("Enter First Number :")
secondNumber=input("Enter Second Number :")
if(inp=="1"):
    print("Result :",int(firstNumber)+int(secondNumber))
elif(inp=="2"):
    print("Result :",int(firstNumber)-int(secondNumber))
elif(inp=="3"):
    print("Result :",int(firstNumber)*int(secondNumber))
elif(inp=="4"):
    print("Result :",int(firstNumber)/int(secondNumber))


