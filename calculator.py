print("Select an operation to perform")

print("1. add")

print("2. Subtract")

print("3. multiply")

print("4. divide")
operation = input()

def AddNums(x,y):
    return x + y

def SubtractNums(x,y):
    return x - y

def MultiplyNums(x,y):
    return x * y

def DivideNums(x,y):    
    if y!= 0:
        return x / y
    else:
        return "Error! Division by zero is not allowed."
    
if operation == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The sum is:", AddNums(num1, num2))

elif operation == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The difference is:", SubtractNums(num1, num2))
    
if operation == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The product is:", MultiplyNums(num1, num2))
    
elif operation == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The quotient is:", DivideNums(num1, num2))
    
    
    
    






