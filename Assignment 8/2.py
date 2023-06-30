def isValid(s):
    def helper(s, count):
        # Base cases
        if count < 0:
            return False
        if not s:
            return count == 0

        # Recursive cases
        if s[0] == '(':
            return helper(s[1:], count + 1)  # Treat '(' as left parenthesis
        elif s[0] == ')':
            return helper(s[1:], count - 1)  # Treat ')' as right parenthesis
        else:
            return (
                helper(s[1:], count) or  # Treat '*' as empty string
                helper(s[1:], count + 1) or  # Treat '*' as left parenthesis
                helper(s[1:], count - 1)  # Treat '*' as right parenthesis
            )

    return helper(s, 0)

# Test case
s = "()"
result = isValid(s)
print(result)
