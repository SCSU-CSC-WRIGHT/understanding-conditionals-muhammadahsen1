# Ask the user for two numbers and an operator 

num1 = float(input("Enter the first number: ")) 

num2 = float(input("Enter the second number: ")) 

operator = input ("Enter an operator (+, -, *, /): ") 

# Perform the corresponding arithmetic operation 

if operator == '+': 

    result = num1 + num2 

print(f"The result of {num1} + {num2} is: {result}") 

if operator == '-': 

    result = numi - num2 

print(f"The result of {num1} - {num2} is: {result}") 

if operator == '*': 

    result = num1 * num2 

    print(f"The result of {num1} * {num2} is: {result}") 

elif operator == '/':

    if num2 != 0: # Check for division by zero 
    
        result = numi / num2 
    
        print(f"The result of {num1} / {num2} is: {result}") 
    
    else: 
    
        print("Error: Division by zero is not allowed.") 

else: 

    print("Error: Invalid operator. Please use +,*, or /.")
