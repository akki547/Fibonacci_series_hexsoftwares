# The Fibonacci series is a sequence where each number is the sum of the two preceding numbers, defined by a mathematical recurrence relationship.

def fibo(n):
    # initialize the first two fibonacci number 
    fibon_ser = []

    a, b = 0,1
    for i in range(n):
        # add the current number to the list 
        fibon_ser.append(a)
        # Update to the next fibonacci number 
        a, b = b, a+b
    
    return fibon_ser


# get the user input for how many fibonacci number to generate
num = int(input("Enter the number of fibonacci number to generate\n"))
# put the condition
if num <= 0:
    print("Please enter a positive number..")
else:
    print("Fibonacci series:", fibo(num))
