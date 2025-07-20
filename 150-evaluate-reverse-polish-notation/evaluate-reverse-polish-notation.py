class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operand_stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b) # truncates toward zero
        }

        for token in tokens:
            if token in operators: 
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = operators[token](operand1, operand2)
                operand_stack.append(result)
            else: # token is an operand
                operand_stack.append(int(token))

        return operand_stack[0]