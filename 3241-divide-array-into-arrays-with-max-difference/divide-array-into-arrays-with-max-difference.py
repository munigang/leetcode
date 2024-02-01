class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums)%3!=0:
            return []
        nums.sort()
        result=[]
        for i in range(0,len(nums),3):
            if i+2<len(nums):
                if nums[i+2]-nums[i]>k:
                    return []
                else:
                     result.append([nums[i],nums[i+1],nums[i+2]])
        return result

