class Solution:        
    def reverse(self, x: int) -> int:
        if (x==0):
            return 0
        elif x > 0:
            x = str(x)
            y = x[-1::-1]
            if y[0]=='0':
                y = int(y)
                if ((-1*pow(2, 31) <= y) and (pow(2, 31)-1) >= y):
                    return y
                else:
                    return 0
            else:
                y = int(y)
                print(y)
                if ((-1*pow(2, 31) <= y) and (pow(2, 31)-1) >= y):
                    return y
                else:
                    return 0
        else:
            x = str(abs(x))
            y = x[-1::-1]
            if y[0]=='0':
                y = int("-"+str(int(y)))
                if ((-1*pow(2, 31) <= y) and (pow(2, 31)-1) >= y):
                    return y
                else:
                    return 0
            else:
                y = int("-"+y[:])
                if ((-1*pow(2, 31) <= y) and (pow(2, 31)-1) >= y):
                    return y
                else:
                    return 0
