class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums=sorted(nums)
        print(nums)
        return_list=[]
        for i in range(0,len(nums),3):
            if nums[i+2]-nums[i]<=k:
                return_list.append([nums[i],nums[i+1],nums[i+2]])
            else:
                return []
        return return_list

        