class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict={}
        for i in s:
            if i in count_dict.keys():
                count_dict[i]=count_dict[i]+1
            else:
                count_dict[i]=1
        count_dict=sorted(count_dict.items(),key=lambda item:item[1],reverse=True)
        result=''
        for k,v in count_dict:
            result+=k*v
        return result

        