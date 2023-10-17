def GetFactorialOfNumber(n):
    Number = 1
    for i in range(1, n+1):
        Number *= i

    return str(Number)


a = int(input())

print("The factorial of number", a, "is:", GetFactorialOfNumber(a))