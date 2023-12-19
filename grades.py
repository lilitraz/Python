# Give me your students' grade and let's do some average games.

grades = [float(input("1: ")), float(input("2: ")), float(input("3: ")), float(input("4: ")), float(input("5: ")), float(input("6: ")), float(input("7: ")), float(input("8: ")), float(input("9: ")), float(input("10: ")), float(input("11: ")), float(input("12: ")), float(input("13: "))]


def print_grades(grades_input):
    for grade in grades_input:
        print(grade)


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
        var = variance / len(scores)
    return var


print(grades_variance(grades))


def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)

print(grades_std_deviation(variance))

for grade in grades:
    print(grade)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
