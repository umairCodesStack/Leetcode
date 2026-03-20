class Solution(object):
    def stableMountains(self, height, threshold):
        stable=[]
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                stable.append(i)
        return stable

print(Solution().stableMountains(height = [10,1,10,1,10], threshold = 3))
