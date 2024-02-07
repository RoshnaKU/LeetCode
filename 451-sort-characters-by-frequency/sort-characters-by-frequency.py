class Solution:
    def frequencySort(self, s: str) -> str:
        count_tup=[(i,s.count(i)) for i in set(s)]
        count_dict=sorted(count_tup,key=lambda item:item[1],reverse=True)
        return "".join([k*v for k,v in count_dict])

        