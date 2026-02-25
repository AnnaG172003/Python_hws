num1, num2, num3 = input("Enter three integer numbers: ").split()
number1 = int(num1)
number2=int(num2)
number3 = int(num3)

if number1 > number2 and number1 > number3:
    print("Maximum number is: ", number1)
elif number2 > number1 and number2 > number3:
    print("Maximum number is: ", number2)
else:
    print("Maximum number is: ", number3)

if number1 < number2 and number1 < number3:
    print("Minimum number is: ", number1)
elif number2 < number1 and number2 < number3:
    print("Minimum number is: ", number2)
else:
    print("Minimum number is: ", number3)