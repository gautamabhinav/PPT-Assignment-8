def minSteps(word1, word2):
    def helper(i, j):
        # Base cases
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        # Recursive cases
        if word1[i] == word2[j]:
            return helper(i + 1, j + 1)  # Characters match, no deletion needed
        else:
            # Delete a character from either word1 or word2
            delete1 = helper(i + 1, j) + 1
            delete2 = helper(i, j + 1) + 1
            return min(delete1, delete2)

    return helper(0, 0)

# Test case
word1 = "sea"
word2 = "eat"
result = minSteps(word1, word2)
print(result)
