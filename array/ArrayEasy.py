def findKOr(self, nums, k):
        res=""
        binaries=[format(x,'032b') for x in nums]
        idx=0
        for x in binaries:  
            while(idx<len(x)):
                count=0
                #print(idx,end="/")
                for y in binaries:
                    if(y[idx]=='1'):
                        count+=1
                if(count>=k):
                    res+='1'
                else:
                    res+="0"
                idx+=1
        return int(res,2)

def minOperations(nums, k):
        count=0
        for x in nums:
             if(x<k):
                  count+=0
        return count
#print(minOperations([2,11,10,1,3],10))


def createTargetArray(self, nums, index):
        res=[]
        for i in range(len(nums)):
             res.insert(index[i],nums[i])
        return res

def numberOfPairs(self, nums1, nums2, k):
        good=0
        for x in nums1:
             for y in nums2:
                if(x%(y*k)==0):
                     good+=1
        return good  

def decompressRLElist( nums):
        ans=[]
        i=0
        while(i<len(nums)):
                freq=nums[i]
                val=nums[i+1]
                i+=2
                for _ in range(freq):
                        ans.append(val)
        return ans                                  

def sumIndicesWithKSetBits(nums, k):
        res=0
        for index in range(len(nums)):  
            count=0
            binary=format(index,'04b')
            for bit in binary:
                if bit=="1":
                        count+=1            
            if(count==k):
               res=res+nums[index]
        return res

def arrayStringsAreEqual(word1, word2):
        result1=""
        result2=""
        for x in word1:
              result1+=x
        for x in word2:
              result2+=x
        return result1==result2

def subarraySum(nums):
        res=0
        for i in range(len(nums)):
              start=max(0,i-nums[i])
              j=start
              add=0
              add=sum(nums[j:i+1]) 
              res+=add
        return res  
              
def numberGame(nums):
      nums.sort()
      i=1
      arr=[]
      while(i<len(nums)):
            arr.append(nums[i])
            arr.append(nums[i-1])
            i+=2
      return arr
    
def restoreString( s, indices):
        indices2=list(indices)
        indices2.sort()
        res=""
        for x in indices2:
              idx=indices.index(x)
              res+=s[idx]
        return res
def countKDifference( nums, k):
      length=len(nums)
      count=0
      for i in range(length):
            j=i+1
            while(j<length):
                res=abs(nums[i]-nums[j])
                j+=1
                if(res==k):
                      count+=1
      return count

def minimumAverage(nums):
      nums.sort()
      stop=int(len(nums)/2)
      j=(stop*2)-1 
      i=0
      arr=[]
      print(nums)
      print(stop)
      while(i<stop & j>=stop):
             add=(nums[i]+nums[j])/2.0
             arr.append(add)
             i+=1
             j-=1
      return min

def twoSum( nums, target):
        arr=[]
        length=len(nums)
        for i in range(length):
              j=i+1
              while(j<length):
                    if(nums[i]+nums[j]==target):
                          arr.append(i)
                          arr.append(j)
                          return arr
                    j+=1

def mapWordWeights(words, weights):
        i=0
        reversedAlphabets=[]  
           
        for i in range(0,26):
              reversedAlphabets.append(chr(i+97))
        alphabets=list(reversedAlphabets)
        reversedAlphabets.reverse()
        res=""
        for word in words:
              ans=0
              for x in word:
                   idx=alphabets.index(x)
                   ans+=weights[idx]
              res+=reversedAlphabets[ans%26]  
        return res         
                     
def countMatches(items, ruleKey, ruleValue):
      ruleIndex = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
      res=0
      for item in items:
            if(item[ruleIndex]==ruleValue):
                  res+=1        
      return res  
def minBitwiseArray(self, nums):
      digitSum=0
      for num in nums:
            digs=getDigits(num)
            digitSum+=sum(digs)
      return abs(digitSum-sum(nums))      
def getDigits(num):
      arr=[]
      while(num!=0):
            arr.append(num%10)
            num=int(num/10)
      return arr      
def countPartitions(nums):
      part1=[]
      part2=[]
      j=0
      n=len(nums)-1
      count=0
      while (j<n):
            part1=nums[0:j+1]
            part2=nums[j+1:n+1]
            j+=1
            if(abs(sum(part1)-sum(part2))%2==0):
                  count+=1
      return count      

def evenNumberBitwiseORs(nums):
        even=[x for x in nums if x%2==0]
        res=even[0]
        for i in range(1,len(even)):
              res=res|even[i]
        return res                     

def sortPeople( names, heights):
      people=[]
      copyHeights=list(heights)
      copyHeights.sort(reverse=True)
      for x in copyHeights:
            idx=heights.index(x)
            people.append(names[idx])
      return people   

def minElement(self, nums):
      digits=[sum(getDigits(x)) for x in nums]
      digis=min(digits)
      return sum(digis)                
                       
def prefixCount(self, words, pref):
      j=len(pref)
      count=0
      for word in words:
            cur=word[0:j]
            if pref in cur:
                  count+=1
      return count  

def earliestTime(self, tasks):
      times=[sum(x) for x in tasks]
      return min(times)

def findIntersectionValues(self, nums1, nums2):
        answer1=0
        answer2=0 
        for x in nums1:
            count=nums2.count(x)
            if(count>0):
                  answer1+=1
                  answer2+=count
        return [answer1,answer2]

def findMissingAndRepeated(nums):
      ans=[]
      count=0
      for i in range(len(nums)):
            count=nums.count(i+1)
            if(count!=1):
                  ans.append(i+1)
      return ans            
            
def getTriplets(nums):
      firstTriplet=nums[0:3]
      a=0
      b=1
      c=2
      triplets=[firstTriplet]
      for i in range(c+1, len(nums)):
            triplets.append([firstTriplet[0],firstTriplet[1],nums[i]])
      return triplets 

def maxArea( height):
      length=len(height)-1
      i=0 
      j=length
      highArea=min(height[i],height[j])*j
      while(i<j):
            if(height[i]<height[j]):
                  area=height[i]*(j-i)
                  i+=1
                  if(area>highArea):
                        highArea=area
            else:
                  area=height[j]*(j-i)
                  j-=1
                  if(area>highArea):
                        highArea=area 
            
      return highArea

def diagonalSum( mat):
      n=len(mat[0])
      i=0
      j=n-1
      s=0
      while(i<n or j>=0):
            if(i!=j):
                  s=s+mat[i][i]+mat[i][j]
            else: 
                  s+=mat[i][i]            
            i+=1
            j-=1
      return s   

def finalPrices( prices):
      answer=[]
      length=len(prices)
      for i in range(length):
            discount=0
            for j in range(i+1,length):
                  if(prices[j]<=prices[i]):
                        discount=prices[j]
                        break
            answer.append(prices[i]-discount)
      return answer            
                         
def isPalendrome(s):
      reverse=s[::-1]
      if (reverse==s):
            return True
      else:
            return False
#print(isPalendrome("ada"))     
#print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
#print(getDigits(15))                   
#print(mapWordWeights( words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
#print(twoSum( nums = [2,7,11,15], target = 9))
def isAnagram(s,t):
      len1=len(s)
      len2=len(t)
      if(len1!=len2):
            return False
      flag=True
      i=0
      while (flag and i<len1):
            cnt=s.count(s[i])
            cnt1=t.count(s[i])
            if (cnt==cnt1):
                  flag=True
            else: 
                  return False
            i+=1      
      return flag
def countWithStrictingElem(nums):
      count=0
      for x in nums:
            if(isStrict(x,nums)):
                  count+=1
      return count            

def isStrict(x,nums):
      rule1=False
      rule2=False
      for i in nums:
            if(i<x):
                  rule1=True
            if(i>x):
                  rule2=True
            if (rule1 and rule2):
                  return True                  
                  
      return True if rule1 and rule2 else False                              
print(isStrict(11,[11,7,2,15]))            