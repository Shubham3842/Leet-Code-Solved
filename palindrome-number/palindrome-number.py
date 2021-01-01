class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=0
        if x<0:
            return False
        else:
            x1 = str(x)
            x2 = str(x)[-1::-1]
            for i in range(len(x1)):
                if x1[i]==x2[i]:
                    c+=1
            if c == len(x1):
                return True
            else:
                return False
