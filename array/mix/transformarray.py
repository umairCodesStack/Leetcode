def transformArray(nums):
    ans=[0 if x%2==0 else 1 for x in nums ]
    ans.sort()
    return ans

print(transformArray([1,5,1,4,2]))