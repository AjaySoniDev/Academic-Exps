num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")
print("// Floor Division")
print("% Modulus")
print("** Exponentiation")

operator=input("\nEnter the operator: ")

if operator=="+":
    print("Result:",num1+num2)

elif operator=="-":
    print("Result:",num1-num2)

elif operator=="*":
    print("Result:",num1*num2)

elif operator=="/":
    if num2!=0:
        print("Result:",num1/num2)
    else:
        print("Division by zero is not allowed")

elif operator == "//":
    if num2 != 0:
        print("Result:", num1//num2)
    else:
        print("Floor division by zero is not allowed")

elif operator=="%":
    if num2!=0:
        print("Result:", num1%num2)
    else:
        print("Modulus by zero is not allowed")

elif operator=="**":
    print("Result:", num1**num2)

else:
    print("Invalid operator!")
