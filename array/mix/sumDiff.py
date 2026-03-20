class Solution(object):
    def leftRightDifference(self, nums):
        leftCur=0
        rightCur=0
        rightSum=[]
        ans=[]
        leftSum=[0]
        j=len(nums)-1
        for i in range(1,len(nums)):
            rightCur+=nums[j]
            j-=1
            leftCur+=nums[i-1]
            leftSum.append(leftCur)
            rightSum.append(rightCur)
        rightSum.reverse()
        rightSum.append(0)
        print(leftSum)
        print(rightSum)
        for i in range(len(leftSum)):
            ans.append(abs(leftSum[i]-rightSum[i]))
        return ans


print(Solution().leftRightDifference([10,4,8,3]))