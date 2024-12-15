def ispalindrome(s):
    s=''.join(e for e in s if e.isalnum()).lower()
    return s==s[::-1]
s=input()
if (ispalindrome(s)):
    print("True")  
else:
    print("False");    