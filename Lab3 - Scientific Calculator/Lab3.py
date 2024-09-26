import math

result = 0.0
menu = 1000

number_of_calc = 0
sum_of_calc = 0
average_of_calc = 0



print(f"Current Result: {result}")
first_operand = 0
second_operand = 0

def firstOperand(first, Result):
    first = (input("Enter first operand: "))
    if (first!= "RESULT"):
        first = float(first)
    # if first.isnumeric():
    #     index = (first.find("-"))
    #     if (index!=-1):
    #         first = float(first)*-1
    #     else:
    #         first = float(first)
    else:

        first = Result

    return first

def secondOperand(second, Result):
    second = (input("Enter second operand: "))
    if (second!= "RESULT"):
        second = float(second)
    # if second.isnumeric():
    #     index = (second.find("-"))
    #     if (index != -1):
    #         second = float(second) * -1
    #     else:
    #         second = float(second)
    else:

        second = Result

    return second

while(menu != 0):
    print()
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")
    print()
    menu = float(input("Enter Menu Selection: "))
    if(menu == 1):
        first_operand = firstOperand(first_operand, result)
        second_operand = secondOperand(second_operand, result)

        result = first_operand + second_operand
        print()
        print(f"Current Result: {result}")
        number_of_calc+=1
        sum_of_calc += result

    elif(menu==2):
        first_operand = firstOperand(first_operand, result)

        second_operand = secondOperand(second_operand, result)

        result = first_operand - second_operand
        print()
        print(f"Current Result: {result}")
        number_of_calc += 1
        sum_of_calc += result
    elif (menu == 3):
        first_operand = firstOperand(first_operand, result)
        second_operand = secondOperand(second_operand, result)
        result = first_operand * second_operand
        print()
        print(f"Current Result: {result}")
        number_of_calc += 1
        sum_of_calc += result
    elif(menu==4):
        first_operand = firstOperand(first_operand, result)
        second_operand = secondOperand(second_operand, result)
        result = first_operand / second_operand
        print()
        print(f"Current Result: {result}")
        number_of_calc += 1
        sum_of_calc += result
    elif (menu == 5):
        first_operand = firstOperand(first_operand, result)
        second_operand = secondOperand(second_operand, result)
        result = math.pow(first_operand, second_operand)
        print()
        print(f"Current Result: {result}")
        number_of_calc += 1
        sum_of_calc += result

    elif(menu == 6):
        first_operand = firstOperand(first_operand, result)
        second_operand = secondOperand(second_operand, result)
        result = math.log(second_operand, first_operand)
        print()
        print(f"Current Result: {result}")
        number_of_calc += 1
        sum_of_calc += result
    elif(menu == 7):

        if(number_of_calc == 0):
            print("Error: No calculations yet to average!")
            menu = int(input("Enter Menu Selection: "))
            if (menu == 0):
                break
        else:
            print(f"Sum of calculations: {sum_of_calc}")
            print(f"Number of calculations: {number_of_calc}")
            average_of_calc = sum_of_calc/number_of_calc
            average_of_calc = round(average_of_calc,2)
            print(f"Average of calculations: {average_of_calc}")
            menu = int(input("Enter Menu Selection: "))

    else:
        if(menu == 0):
            pass
        else:
            print("Error: Invalid selection!")
            menu = int(input("Enter Menu Selection: "))
            if (menu == 0):
                break

print("Thanks for using this calculator. Goodbye!")