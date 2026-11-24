class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            
            elif stack and stack[-1] == '(' and s[i] == ')':
                stack.pop()
            
            elif stack and stack[-1] == '[' and s[i] == ']':
                stack.pop()
            
            elif stack and stack[-1] == '{' and s[i] == '}':
                stack.pop()
            
            else:
                return False
        
        return True if len(stack) == 0 else False