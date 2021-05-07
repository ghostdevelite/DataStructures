"""without importing the stack class, this is how you convert integer to binary
"""


def div_by_2(dec_num):
    stack = []

    while dec_num > 0:
        remainder = dec_num % 2
        stack.append(remainder)
        dec_num = dec_num //2


    bin_num  = ""
    while not stack == []:
        bin_num += str(stack.pop())

    return  bin_num

print(div_by_2(121))
