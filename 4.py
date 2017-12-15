def isPalindrome(num):
    s = str(num)
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

ans = 0
for i in range(999, 0, -1):
    for j in range(999 ,0, -1):
        if isPalindrome(i*j):
            ans = max(ans, i*j)
#            exit()
print ans
