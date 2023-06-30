from collections import Counter

def findAnagrams(s, p):
    result = []
    window_size = len(p)
    target_count = Counter(p)
    window_count = Counter(s[:window_size])

    if window_count == target_count:
        result.append(0)

    for i in range(1, len(s) - window_size + 1):
        # Update the window count by removing the character at the previous window's start and adding the character at the current window's end
        window_count[s[i - 1]] -= 1
        if window_count[s[i - 1]] == 0:
            del window_count[s[i - 1]]

        window_count[s[i + window_size - 1]] += 1

        if window_count == target_count:
            result.append(i)

    return result




s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)
