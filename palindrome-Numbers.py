class Solution:
    def isPalindrome(self, x):
        mystr = str(x)
        for i in range(len(mystr)//2):
            if mystr[i] == mystr[~i]:
                continue
            else:
                return False
        return True