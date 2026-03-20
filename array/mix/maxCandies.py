class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxN=max(candies)
        res=[True if x+extraCandies>=maxN else False for x in candies]
        return res

print(Solution().kidsWithCandies( candies = [4,2,1,1,2], extraCandies = 1))