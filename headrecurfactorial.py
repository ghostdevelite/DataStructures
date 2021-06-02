


def factorial(num):

    #base case 01=1
    if num == 0:
        return 1


    #recursion
    result1 = factorial(num-1)

    #operator
    result2 = num * result1
    return result2

print(factorial(5))
