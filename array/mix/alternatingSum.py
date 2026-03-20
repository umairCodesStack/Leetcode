def alternatingSum(nums):
    sum=nums[0]
    for i in range(1,len(nums)):
        if(i%2==0):
            sum+=nums[i]
        else:
            sum-=nums[i]
    return sum
print(alternatingSum([1,3,5,7]))