num1=int(input("Enter the first number :"))
num2=int(input("Enter the Second Number :"))
operation=input("Enter the Operations:- +,-,*,/,%,** : ")

if(operation == "+"):
    print("The Sum Is :",num1+num2)
elif(operation == "-"):
    print("The Sub is :",num1-num2)
elif(operation == "*"):
    print("The Mul is :",num1*num2)
elif(operation == "/"):
    print("The Div is :",num1/num2)
elif(operation== "**"):
    print("The mod is :",num1%num2)
else:
    print("Invalid Operation")