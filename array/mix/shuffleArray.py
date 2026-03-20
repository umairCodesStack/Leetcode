def shuffle(nums, n):
    ans=[]
    j=n
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[j])
        j+=1
    return ans

print(shuffle([1,2,3,4,4,3,2,1], n = 4))
