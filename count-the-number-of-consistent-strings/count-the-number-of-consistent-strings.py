class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = list(allowed)
        word = list(set(list(''.join(words))))
        result = list(set(word) - set(allowed))
        c=0
        res = 0
        if len(result) == 0:
            res =len(words)-c
        else:
            for i in words:
                for j in result:
                    if j in i:
                        c+=1
                        break
            res = len(words)-c
        return res    
