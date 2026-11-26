class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        stack = []

        for i in range(n):
            if tokens[i] in '+-*/':
                a = stack.pop()
                b = stack.pop()

                if tokens[i] == '+':
                    stack.append(b + a)

                elif tokens[i] == '-':
                    stack.append(b - a)

                elif tokens[i] == '*':
                    stack.append(b * a)

                elif tokens[i] == '/':
                    result = abs(b) // abs(a)
                    if (b < 0) != (a < 0):
                        result = -result
                    stack.append(result)

            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]