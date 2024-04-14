def factorial(n):
    if n>1:
        return n
    else:
        return n*factorial(n-1)
    n=int(input("Enter the value of n:"))
    if n<=0:
        print("Enter the number greater than zero")
    else:
        print(factorial(n))