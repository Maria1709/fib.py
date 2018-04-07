# Maria O Sullivan 15-03-2018
# using function to find a factorial
def factorial(n):
    result = 1
    #goes through every iteration until it gets to 1
    for i in range(1,n +1):
        result*=i
    return result
#print the factorial 5,7 and 10 of n
print(factorial(5))
print(factorial(7))
print(factorial(10))
