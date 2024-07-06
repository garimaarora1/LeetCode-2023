class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = '+-*/'
        stack = []
        for token in tokens:
            
            if token in operands:
                first = stack.pop()
                second = stack.pop()
                if token ==  '+':
                    stack.append(second+first)
                elif token == '/':
                    stack.append(int(second/first))
                elif token == '-':
                    stack.append(second-first)
                elif token == '*':
                    stack.append(second*first)

            else:
                stack.append(int(token))
        return stack[-1]
        