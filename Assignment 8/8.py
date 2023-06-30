def canSwapStrings(s, goal):
    def swapHelper(s, goal, i, j):
        if s == goal:
            return True
        
        if i >= len(s) or j >= len(s):
            return False
        
        if s[i] == goal[i] and s[j] == goal[j]:
            return swapHelper(s, goal, i+1, j+1)
        
        if s[i] == goal[j] and s[j] == goal[i]:
            new_s = list(s)
            new_s[i], new_s[j] = new_s[j], new_s[i]
            return swapHelper("".join(new_s), goal, i+1, j+1)
        
        return False
    
    return swapHelper(s, goal, 0, 1) or swapHelper(s, goal, 1, 0)


s = "ab"
goal = "ba"
result = canSwapStrings(s, goal)
print(result)
