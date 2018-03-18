# Maria O Sullivan
# using function to find a factorial
def factorial(n):
    result = 1
    for i in range(1,n +1):
        result*=i
    return result

print(factorial(5))
print(factorial(7))
print(factorial(10))
