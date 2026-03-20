class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            index=getMinNumIndex(nums)
            print(index)
            nums[index]=nums[index]*multiplier
            print(nums)
        return nums
    
def getMinNumIndex(nums):
        index=0
        min=nums[index]
        for i in range(1,len(nums)):
            if nums[i]<min:
                min=nums[i]
                index=i
        return index

print(Solution().getFinalState(nums = [1,5,2], k = 4, multiplier = 4))        
#print(Solution.getMinNumIndex([2,1,3,5,6]))