class Solution:
    def isValid(self, s: str) -> bool:
        l={'(':')','[':']','{':'}'}
        a=[]
        for i in s:
            if len(a)>=1 and a[-1] in l.keys() and l[a[-1]]==i:
                    a.pop()
            else:
                a.append(i)
        #print(a)
        return True if len(a)==0 else False
                





    

        