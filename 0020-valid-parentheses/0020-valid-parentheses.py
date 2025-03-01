class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching = {')': '(', '}': '{', ']': '['}
        stack = []  # Use a stack to track opening parentheses

        for char in s:
            if char in matching.values():  # If it's an opening bracket
                stack.append(char)
            elif char in matching.keys():  # If it's a closing bracket
                if stack and stack[-1] == matching[char]:
                    stack.pop()  # Pop the matching opening bracket
                else:
                    return False  # Invalid if no match or mismatched
        return len(stack) == 0

        