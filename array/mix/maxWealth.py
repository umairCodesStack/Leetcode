class Solution(object):
    def maximumWealth(self, accounts):
        newList=[]
        for x in accounts:
            newList.append(sum(x))  
        return max(newList)

print(Solution().maximumWealth([[1,2,3],[3,2,1]]))