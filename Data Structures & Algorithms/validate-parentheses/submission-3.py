class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return -1

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return -1

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = Stack()
        for e in s:
            if e == '(' or e == '{' or e == '[':
                stack.push(e)
            elif e == ')':
                t = stack.peek()
                if t == -1 or t != '(':
                    return False
                elif t == '(':
                    t = stack.pop()
            elif e == '}':
                t = stack.peek()
                if t == -1 or t != '{':
                    return False
                elif t == '{':
                    t = stack.pop()
            elif e == ']':
                t = stack.peek()
                if t == -1 or t!='[':
                    return False
                elif t == '[':
                    t = stack.pop()
        if stack.is_empty():
            return True  
        else:
            return False          

        