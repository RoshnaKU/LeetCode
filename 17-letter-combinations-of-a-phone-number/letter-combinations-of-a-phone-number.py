from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==1:
            return [*d[digits]]
        elif len(digits)==0:
            return []
        else:
            l=[]
            for i in digits:
                l.append(d[i])
            print(l)
            res=[]
            for i in l[0]:
                for j in l[1]:
                    if len(digits)==2:
                        res.append(i+j)
                    elif len(digits)>=3:
                        for k in l[2]:
                            if len(digits)==3:
                                res.append(i+j+k)
                            if len(digits)==4:
                                for m in l[3]:
                                    res.append(i+j+k+m)
            return res
                        
            

                

        