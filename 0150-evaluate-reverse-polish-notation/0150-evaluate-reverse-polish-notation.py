class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands_set = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operands_set:
                second_item = stack.pop()
                first_item = stack.pop()
                
                if token == '+':
                    stack.append(first_item + second_item)
                
                elif token == '-':
                    stack.append(first_item - second_item)
                
                elif token == '/':
                    stack.append(int(first_item / second_item))
                
                elif token == '*':
                    stack.append(first_item * second_item)
            else:
                stack.append(int(token))
        
        return stack[-1]
                
                
            
        