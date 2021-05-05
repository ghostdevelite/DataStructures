
"""This is a stack class using stack algorithm"""


class Stack():

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def remove(self):
        self.items.pop()

    def check_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

s = Stack()
s.push('a')
s.push('b')
print(s.is_empty())
s.push('c')
print(",".join(s.check_stack()))
print(s.peek())



