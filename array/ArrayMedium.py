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

#print(getUniqueWithFreq([-1,2,1,2,3,1]))            
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
def groupAnagrams(srr):
    for i in range(len(srr)-1,-1,-1):
        temp=[]
        temp.append(srr[i])
        #print("i",srr[i])
        for j in range(i-1,-1,-1):
            #print(srr[j])
            if(isAnagram(s=srr[i],t=srr[j])):
                print(srr[j])
                temp.append(srr[j])
                srr.pop(j)
        #print("new srr",srr)        
        print(temp)    
print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
def swap(a,b):
    temp=a
    a=b
def findAnargrams(s,srr):
    ans=[]
    for x in srr:
        if(isAnagram(s=s,t=x)):
            ans.append(x)
            srr.remove(x)
    return ans

#print(getTopKFrequent(nums = [-1,-1], k = 1))   
def getUniques(arr):
    uniqs=[arr[0]]
    for i in range(1,len(arr)):
        temp=arr[0:i]
        if(arr[i] not in temp):
            uniqs.append(arr[i])
    return uniqs
def getTopKFrequent(arr,k):
    uniqs=getUniques(arr)
    NumWithfreqs=[]
    for x in uniqs:
        temp=[]
        temp.append(x)
        temp.append(arr.count(x))
        NumWithfreqs.append(temp)
    NumWithfreqs.sort(key=lambda x: x[1], reverse=True)
    print(NumWithfreqs)
    ans=[x[0] for x in NumWithfreqs[0:k]]
    return ans   

def getTopKElem(nums,k):
    freq={}
    for x in nums:
        freq[x]=freq.get(x,0)+1
    arr=[(key,value) for key,value in freq.items()]
    arr.sort(reverse=True,key=lambda x:x[1])
    return [x[0] for x in arr[0:k]]

print(getTopKElem([-1,1,2,1,4,4,1,3],2))
#print(getTopKFrequent([-1,1,2,1,4,4,1,3],2))       
def jewelsProb(js,stn):
    freq={}
    for x in js:
        freq[x]=0
    print(freq)
    for x in freq:
        freq[x]=stn.count(x)
    return sum(freq.values())    
def jewelsProb2(jewels,stones):
    freq={}
    for x in stones:
        if x in jewels:
            freq[x]=freq.get(x,0)+1
    print(freq)  
    return sum(freq.values())  
print(jewelsProb2("aA","aAAbbbb"))    
def maxFreqSum(s: str) -> int:
    vowels="aeiou"
    freq1={}
    freq2={}
    for x in s:
        if x in vowels:
            freq1[x]=freq1.get(x,0)+1
        else:
            freq2[x]=freq2.get(x,0)+1
        arr1=[0]
        arr2=[0]
                
    return max(freq1.values())+max(freq2.values())            
print(maxFreqSum("aeioiu"))

def threeSum(arr,target):
    length=len(arr)
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if(arr[i]+arr[j]+arr[k]==target):
                    ans=[arr[i],arr[j],arr[k]]
    return ans                

def longestConsective(nums):
    prev=nums[0]
    length=len(nums)
    i=1
    maxLen=0
    nums.sort()
    while i<length:
        temp=[prev]
        while nums[i]==prev+1:
            temp.append(nums[i])
            i+=1
        maxLen=max(len(temp),maxLen)
        i+=1    
    return maxLen
