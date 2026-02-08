def add(a, b):
    print("add", a + b)
def subtract(a, b):
    print("subtract", a - b)
def multiply(a, b):
    print("multiply", a * b)
def divide(a, b):
    print("divide", a / b)

print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = int(input(" choice (1-4): "))
a = int(input("First number: "))
b = int(input("Second number: "))
if choice == 1:
    add(a,b)
    
elif choice ==2:
    subtract(a,b)
    
elif choice ==3:
    multiply(a,b)
     
elif choice ==4:
    divide(a,b)
    
else :
    print("wrong input")  
