# METHOD 1 (more efficient)
# def isPalindrome(s):
#     ss =""
#     for ch in s:
#         if ch.isalpha():
#             ss += ch
#     res = ""
#     for ch in s:
#         if ch.isalpha():
#             res += ch
#     return ss.lower() == res[::-1].lower()
# s = "race a ecar"
# print(isPalindrome(s))


# METHOD 2 
def isPalindrome(s):
    l,r = 0,len(s)-1

    while l<r:
        while l<r and not isalphanum(s[l]):
            l+=1
        while r>l and not isalphanum(s[r]):
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l,r = l+1,r-1 
    return True

def isalphanum(c):
    return (ord('A'))<=ord(c)<=ord('Z') or ord('a') <=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9') 
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))









# METHOD 1
# def isPalindrome(s):
#     ss =""
#     for ch in s:
#         if ch.isalpha():
#             ss += ch
#     res = ""
#     for ch in s:
#         if ch.isalpha():
#             res += ch
#     return ss.lower() == res[::-1].lower()
# s = "race a ecar"
# print(isPalindrome(s))