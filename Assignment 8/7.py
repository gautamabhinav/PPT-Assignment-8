def decodeString(s):
    def decodeHelper(s, i):
        decoded = ""
        while i < len(s) and s[i] != ']':
            if not s[i].isdigit():
                decoded += s[i]
                i += 1
            else:
                # Get the repetition count
                count = 0
                while s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i += 1
                
                # Skip the opening bracket '['
                i += 1
                
                # Decode the enclosed string recursively
                sub_str, i = decodeHelper(s, i)
                
                # Repeat the decoded string
                decoded += sub_str * count
                
                # Skip the closing bracket ']'
                i += 1
        
        return decoded, i
    
    return decodeHelper(s, 0)[0]




s = "3[a]2[bc]"
result = decodeString(s)
print(result)
