def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
     if num2 == 0:
        return "Error: Cannot divide by zero"
    else:
        return num1 / num2

def multiply(num1, num2):
    return num1*num2

while True:
    print("\nSelect operation:")
print("1. add")
print("2. subtract")
print("3. divide")
print("4. multiply")

choice = input("enter choice(1/2/3/4): ")

 if choice in ('1', '2', '3', '4'):
    num1 = float(input("enter first number:" ))
    num2 = float(input("enter second number:" ))



if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)    
elif choice == '3':
    result = divide(num1, num2)
elif choice == '4':
    result = multiply(num1, num2)
    
    print(result)   
    
 elif choice == '5':
        print("Exiting calculator...")
        break
    else:
        print("Invalid input. Please select a valid option.")   
      