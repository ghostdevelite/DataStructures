

def fibhead(num):

    if num == 0:
        return 0
    if num == 1:
        return 1
    
    #head recursion
    fib = fibhead(num-1)
    fib2 = fibhead(num-2)
    #operations
    result2 = fib + fib2
    return result2


def fibtail(num,a=0,b=1):
    #Accumulators are used in tail recursion as a way of communicating a partial result down through 
    #the recursive call chain without requiring extra space to be used at each level of the recursion
    if num == 0:
        return a

    if num == 1:
        return b

    return fibtail(num-1,b,a+b)


print(fibtail(6))
print(fibhead(6))
