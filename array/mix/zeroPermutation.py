def buildArray( nums):
    ans=[]
    for index in range(len(nums)):
        ans.append(nums[nums[index]])
    return ans

def buildArray2(nums):
    ans=[nums[nums[x]] for x in range(len(nums))]
    return ans

print(buildArray2([0,2,1,5,3,4]))