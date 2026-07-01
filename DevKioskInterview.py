def findTwoSum(nums , target):
    ans=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j]==target):
                ans=[i,j]
                return ans
    return ans 
print(findTwoSum(nums = [3,2,4] ,target = 6))           
def isPalendrome(s):
    reverse=s[::-1]
    return s==reverse
print(isPalendrome("hello"))
def moveZerosToEnd(nums):
    j=len(nums)-1
    i=0
    while(i<j):
        if(nums[i]==0):
            temp=nums[j]
            nums[j]=nums[i]
            nums[i]=temp
            j-=1
        i+=1    
    return nums        
print(moveZerosToEnd([0,1,0,3,12]))
def find2ndLargest(nums):
    maxNum=nums[0]
    secondMax=False
    for i in range(1, len(nums)):
        if nums[i]>maxNum:
            secondMax=maxNum
            maxNum=nums[i]
    return "No Second Max" if secondMax==False else secondMax        

print(find2ndLargest([10,20,4,45,99]))
def getUniqueChars(s):
    prev=s[0]
    res=[]
    res.append(prev)
    for i in range(1,len(s)):
        if (s[i]!=prev):
            prev=s[i]
            res.append(s[i])
    return res
def characterCount(s):
    uniques=getUniqueChars(s)
    mpp={}
    for x in uniques:
        mpp.update({x:s.count(x)})
    return mpp

print(characterCount("programming"))
def sumUptoN(n):
    series=[1,2,3,4]
    ans=0
    if(n<5):
        return series[n-1]
    if(n<5):
        ans=sum(series[0:n])
    else:
        i=4
        while(i<n):
            ans=sum(series[-4:len(series)])
            series.append(ans)
            i+=1
    return ans        

print(sumUptoN(6))
arr=[1,2,3,4,5,6,7,8]
length=len(arr)
i=0
while i<length:
    if(arr[i]%2==0):
        arr.remove(arr[i])
        length=len(arr)
        i-=1
    i+=1        
print(arr)    
