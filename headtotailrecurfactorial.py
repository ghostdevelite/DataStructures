

def headrecur(num):

    if num == 1:
        return 1

    result1 = headrecur(num-1)

    result2 = num * result1
    return result2


def tailrecur(num, accumulator=1):

    if num == 1:
        return accumulator

    return tailrecur(num-1, num * accumulator)

print(tailrecur(5))


