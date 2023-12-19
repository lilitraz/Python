def sum(n):
    result = 0
    while n > 0:
        digit = n % 10
        n //= 10
        result += digit
    return(result)

try:
    x = int(input("select a number: "))
    res = sum(x)
    print(f"sum of digits of {x} is {res}")
except ValueError:
    print("Sorry, you need to type a number")