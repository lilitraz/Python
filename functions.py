def digit_sum(n):

    total = 0
    for i in n:
      n = int(n)
      i = int(i)
      total += i


digit_sum(1234)


def is_prime(x):
  if x < 2:
    return False
  else:
    for n in range(2, x-1):
        if x % n == 0:
          return False
  return True


def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word


print(reverse("Hello World"))


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrubble_score(word):
    word = word.lower()
    result = 0
    for letter in word:
      result += score[letter]
    print(result)

scrubble_score("pizza")

def count(sequence, item):
    result = 0
    for i in sequence:
      if i == item:
        result += 1
    return result

print(count([4, 5, 5, 2, 6], 5))


