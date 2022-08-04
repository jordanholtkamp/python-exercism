from logging import raiseExceptions


def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    i = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            i += 1
        else:
            number = number * 3 + 1
            i += 1 
    return i
