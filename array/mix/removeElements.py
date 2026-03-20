class Solution(object):
    def removeElement(self, nums, val):
        k=0

        for x in range(len(nums)):
            if(nums[x]!=val):
                k+=1
                
            
        return k
    


print(Solution().removeElement( nums = [0,1,2,2,3,0,4,2], val = 2))