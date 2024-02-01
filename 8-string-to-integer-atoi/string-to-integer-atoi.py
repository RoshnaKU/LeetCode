class Solution:
    def myAtoi(self, s: str) -> int:
        clean=s.strip()
        if len(clean)==0 or clean in ['+','-'] or clean[0].isalpha():
            return 0
        if clean[0] in ['+','-'] and not clean[1].isdigit():
            return 0
        if clean[0]=='.':
            return 0
        s=''        
        for i in range(len(clean)):
            if i==0 and (clean[i].isdigit() or clean[i] in ['+','-']):
                s+=clean[i]
            elif i!=0 and clean[i].isdigit():
                s+=clean[i]
            else:
                break
        print(s)
        if (-2**31)>int(s):
            return (-2**31)
        elif int(s)> (2**31)-1:
            return (2**31)-1
        else:
            return int(s)