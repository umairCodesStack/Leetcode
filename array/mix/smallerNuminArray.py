class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans=[0 for x in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]>nums[j]):
                    ans[i]+=1
                elif(nums[i]<nums[j]):
                    ans[j]+=1
        return ans
    def smallerNumberslogic2(self, nums):
        nums.sort()
        ans=[]
        length=len(nums)
        for x in range(length):
            ans.append(length-x)
        print(4^2)
        return ans




print(Solution().smallerNumberslogic2([6,5,4,8]))        