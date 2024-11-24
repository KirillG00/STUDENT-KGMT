def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
 
 
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
 
 
operation = select_operation(1)   
print(operation(8, 7))            
 
operation = select_operation(2)    
print(operation(8, 7))           
 
operation = select_operation(3)    
print(operation(8, 7))            