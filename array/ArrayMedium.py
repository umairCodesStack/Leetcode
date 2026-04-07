def getFrequencies(nums):
    ans=[]
    maxNum=max(nums)
    for i in range(maxNum+1):
        ans.append(nums.count(i))
    return ans 

def getTopKFrequent(nums,k):
    freqs=getFrequencies(nums)
    ans=[]
    print(freqs)
    maxNum=max(freqs)
    a=freqs.index(maxNum)
    #print(a)
    ans.append(a) 
    freqs.remove(maxNum)   
    for i in range(1,k):
        maxNum=max(freqs)
        a=freqs.index(maxNum)
        #print(a+1)
        ans.append(a+1)
        freqs.remove(maxNum)

    return ans 

def getUniqueWithFreq(nums):
    mpp={}
    for x in nums:
        keys=mpp.keys()
        if x not in keys:
            mpp.update({x:1})
        else:
            mpp[x]=mpp[x]+1
    return mpp

print(getUniqueWithFreq([-1,2,1,2,3,1]))            
def isAnagram( s: str, t: str) -> bool:
        arr1=[x for x in s]
        arr2=[x for x in t]
        if (len(arr1)!=len(arr2)):
            return False
        arr1.sort()
        arr2.sort()
        if (arr1==arr2):
            return True
        return False    

def findAnargrams(s,srr):
    ans=[]
    temp=srr
    for x in temp:
        if(isAnagram(s=s,t=temp)):
            ans.append(x)
            temp.remove(x)
    return ans
print(findAnargrams(s="act",srr=["act","pots","tops","cat","stop","hat"]))
#print(getTopKFrequent(nums = [-1,-1], k = 1))   