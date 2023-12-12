def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

num1 = float(input("Please enter the number: "))

print("The factorial of the number is "+ str(factorial(num1)))
