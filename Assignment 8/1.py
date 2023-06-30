def minimumDeleteSum(s1, s2, i, j, memo):
    # Base cases
    if i == len(s1) and j == len(s2):
        return 0
    if i == len(s1):
        return sum(ord(ch) for ch in s2[j:])
    if j == len(s2):
        return sum(ord(ch) for ch in s1[i:])

    # Check if the result is already memoized
    if (i, j) in memo:
        return memo[(i, j)]

    if s1[i] == s2[j]:
        # Characters match, no deletion required
        memo[(i, j)] = minimumDeleteSum(s1, s2, i + 1, j + 1, memo)
    else:
        # Delete one character from either s1 or s2
        delete_s1 = ord(s1[i]) + minimumDeleteSum(s1, s2, i + 1, j, memo)
        delete_s2 = ord(s2[j]) + minimumDeleteSum(s1, s2, i, j + 1, memo)
        memo[(i, j)] = min(delete_s1, delete_s2)

    return memo[(i, j)]

# Test case
s1 = "sea"
s2 = "eat"
memo = {}
result = minimumDeleteSum(s1, s2, 0, 0, memo)
print(result)
