def wordsCount(s):
    arr=s.split(" ")
    mpp={}
    for x in arr: 
        mpp[x]=mpp.get(x,0)+1
    return mpp 
def thirdHigh(nums):
    nums.sort(reverse=True)
    return nums[2]
def getMax(nums):
    maximum=nums[0]
    for i in range(1,len(nums)):
        if (nums[i]>maximum):
            maximum=nums[i]
    return maximum
def thirdMax(nums):
    maximum=getMax(nums)
    nums.remove(maximum)
    max2=getMax(nums)
    nums.remove(max2)
    return getMax(nums)
def firstWordCap(s):
    arr=s.split(" ")
    ans=""
    for x in arr:
        temp=x[0].upper()
        temp+=x[1:]
        ans+=temp
        ans+=" "    
    return ans               
#print(firstWordCap("hello world from oka"))
# print(thirdMax([12,34,22,33,45,56,100,1,300]))          
#print(wordsCount("The cat sat on the mat.The cat is fat"))


def targetSum(nums,target):
    length=len(nums)
    ans=[]
    for i in range(length):
        for j in range(i+1,length):
            if (nums[i]+nums[j]==target):
                ans.append(i)
                ans.append(j)
                return ans
            
print(targetSum(nums = [3, 2, 4], target = 6))            