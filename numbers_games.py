from random import randint
from math import lcm
import math

# 1. Choose 10 numbers, I will show you the largest one you chose.

largest = float("-inf")

for _ in range(10):
    number = float(input("choose a number: "))
    if number > largest:
        largest = number

print(largest)

# 2. Tell me your age in years, I will tell you it in months.

while True:
    try:
        age = (input("whats your age? "))
        if age.isalpha():
            print("please enter numbers only!")
        else:
            age = float(age)
            print("this is your age in months: ", (age * 12))
    except ValueError:
        print("please enter numbers only!")
    break

# 3. Write some texts. When you want me to repeat them on REVERSE order, enter an empty line.

text = " "
while True:
        line = input("enter text: ")
        if len(line) == 0:
            break

        text = line + "\n" + text

print(text)

# 4. I'm rolling numbers until I get one that divides by 7, 13 and 15. Then I'll show you that number.

while True:
    guess = randint(1, 1000000)
    if guess % 7 == 0 and guess % 13 == 0 and guess % 15 == 0:
        break

print(guess)

# 5. I'll give you two random numbers and their least common multiple.

n1 = randint(1, 10)
n2 = randint(1, 10)

print("your numbers: ", n1, n2 )
print(math.lcm(n1, n2))

# 6. Let's play a game! Guess my number. I will help you get to it. Notice - sometimes I'm lying ;)

secret = randint(1, 100)

while True:
    guess = int(input("Guess a number: "))
    if guess == secret:
        print("Bravo!")
        break

    lying = randint(1, 100) < 10

    if lying:
        if guess > secret:
            print("too small ;)")
        elif guess < secret:
            print("too big ;)")
    else:
        if guess > secret:
            print ("too big")
        elif guess < secret:
            print("too small")