class Solution:
    def frequencySort(self, s: str) -> str:
        valid_input = list(string.ascii_lowercase)+list(string.ascii_uppercase)+[0,1,2,3,4,5,6,7,8,9]
        count_dict={}
        for i in s:
            if i in count_dict.keys():
                count_dict[i]=count_dict[i]+1
            else:
                count_dict[i]=1
        print(count_dict)
        count_dict=sorted(count_dict.items(),key=lambda item:item[1],reverse=True)
        result=''
        for k,v in count_dict:
            result+=k*v
        return result

        