class Solution(object):
    def countPairs(self, nums, target):
        goodpairs=0
        for i in range(len(nums)):
            cur=nums[i]
            for j in range(i + 1, len(nums)):
                if(cur+nums[j]<target):
                    goodpairs+=1
                  
        return goodpairs

print(Solution().countPairs( [-6,2,5,-2,-7,-1,3], target = -2))