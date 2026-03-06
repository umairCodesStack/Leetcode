def getSneakyNumbers(nums):
        sneakyNums=[]
        for i in range(len(nums)):
            cur=nums[i]
            restarray=nums[i+1:len(nums)]
            if cur in restarray:
                sneakyNums.append(cur)
        return sneakyNums
    
print(getSneakyNumbers([0,1,1,0]))
        