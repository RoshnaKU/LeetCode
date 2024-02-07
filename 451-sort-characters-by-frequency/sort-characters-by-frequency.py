class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict={i:s.count(i) for i in set(s)}
        count_dict=sorted(count_dict.items(),key=lambda item:item[1],reverse=True)
        result=''
        for k,v in count_dict:
            result+=k*v
        return result

        