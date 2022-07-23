class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(operator, x, y):
            x = int(x)
            y = int(y)
            if operator == "+":
                return x + y
            if operator == "*":
                return x * y
            if operator == "/":
                return int(x / y)
            else:
                return x - y

        check = {"+", "*", "/", "-"}
        i = 0
        while len(tokens) != 1:
            if tokens[i] in check:
                tokens[i - 2] = operation(tokens[i], tokens[i - 2], tokens[i - 1])
                tokens.pop(i)
                tokens.pop(i - 1)
                i = i - 2
            else:
                i += 1

        return tokens[0]
