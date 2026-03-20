class Solution(object):
    def decode(self, encoded, first):
        cur=first
        ans=[first]
        for x in encoded:
            cur=cur^x
            ans.append(cur)
        return ans

print(Solution().decode( encoded = [6], first = 1))