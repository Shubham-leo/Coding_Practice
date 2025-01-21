def isValid(s):
    stack1 = []
    hashm={")":"(","]":"[","}":"{"}

    for i in s:
        if i in hashm:
            if stack1 and stack1[-1]==hashm[i]:
                stack1.pop()
            else:
                return False
        else:
            stack1.append(i)
    
    return True if not stack1 else False

s = "()"
print(isValid(s))
