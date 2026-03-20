class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0
        flag=False
        for word in words:
            for a in word:
                if a in allowed:
                    flag=True
                else:
                    flag=False
                    break
            if(flag==True):
                count+=1        
        return count

print(Solution().countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))