def minimumOperations(nums):
    operations=0
    for x in nums:
        if x%3!=0:
            operations=operations+1
         
            
    return operations

print(minimumOperations([1,2,3,4]))