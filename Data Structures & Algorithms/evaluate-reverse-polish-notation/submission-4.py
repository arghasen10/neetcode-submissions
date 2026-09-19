class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        input_stack = []
        for elem in tokens:
            if elem == "+":
                b = input_stack.pop()
                a = input_stack.pop()
                input_stack.append(int(a+b))
            elif elem == "-":
                b = input_stack.pop()
                a = input_stack.pop()
                input_stack.append(int(a-b))
            elif elem == "*":
                b = input_stack.pop()
                a = input_stack.pop()
                input_stack.append(int(a*b))
            elif elem == "/":
                b = input_stack.pop()
                a = input_stack.pop()
                input_stack.append(int(a/b))
            else:
                input_stack.append(int(elem))
        return input_stack.pop()