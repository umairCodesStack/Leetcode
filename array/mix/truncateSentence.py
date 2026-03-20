class Solution(object):
    def truncateSentence(self, s, k):
        ans=""
        j=len(s)-1
        wordsToSkip=(s.count(" ")+1)-k
        word=0
        while(word<wordsToSkip):
            if(s[j]==" "):
                word+=1
            j-=1
        ans=s[0:j+1]
        return ans
print(Solution().truncateSentence("Hello how are you Contestant",5))


def mostWordsFound(sentences):
        words=[x.count(" ")+1 for x in sentences]
        return max(words)

print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))
             