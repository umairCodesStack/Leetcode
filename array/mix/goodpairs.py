def numIdenticalPairs(nums):
    goodpairs=0
    for i in range(len(nums)):
        cur=nums[i]
        for j in range(i + 1, len(nums)):
            if(cur==nums[j]):
                goodpairs+=1
                  
    return goodpairs

print(numIdenticalPairs( [1,2,3,1,1,3]))