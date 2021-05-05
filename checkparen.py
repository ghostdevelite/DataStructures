


my_dict = {
    
    '[':']',
    '{':'}',
    '(':')'

}

def check(paren):
    stack = []

    for value in paren:
        if value in my_dict:
            stack.append(value)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0

print(check('()'))
