def count( head, key):
        freq=0
        curNode=head
        while curNode is not None:
            if(curNode.data==key):
                freq+=1
            curNode=curNode.next
        return freq
def reverseList(head):
    arr=[]
    while head is not None:
         arr.append(head)
         head=head.next
    lenght=len(arr)
    head2=arr[lenght]
    head2.next=arr[lenght-1]
    cur=arr[lenght-1]
    for j in range(lenght-2,-1,-1):
        cur.next=arr[j]
        cur=arr[j]     
    return head2 

def getKthFromLast(self, head, k):
    length=getLength(head)
    nth=length-k-1
    temp=head
    j=0
    while(j!=nth):
        temp=temp.next
        j+=1
    res=temp.next
    return res
def getLength(head):
    i=0
    cur=head
    while(cur.next is not None):
        i+=1
        cur=cur.next
    return i
def longestNonRepStr(s):
    i=0
    maxLength=0
    while(i<len(s)):
        temp=[]
        j=i
        while(s[j] not in temp):
            temp.append(s[j])
            j+=1
        i=j
        length=len(temp)-1
        if(length>maxLength):
            maxLength=length
    return maxLength
#print(longestNonRepStr("abcerrrrr"))        
def longestSeq(arr):
    i=min(arr)
def longestConsecutive( nums):
        if(len(nums)==0):
            return 0
        nums.sort()
        y=nums[0]
        i=1
        maxCnt=0
        while(i<len(nums)):
            cnt=1
            j=i
            while(j<len(nums)):
                if(nums[j]==y+1):
                    cnt+=1
                    j+=1
                    y=nums[j]
                j+=1
            i+=1  
            if cnt>maxCnt:
                maxCnt=cnt
        return maxCnt  
print(longestConsecutive([100,4,200,1,3,2]))
def removeDuplicates(head):
    prev=None
    cur=head
    while cur.next is not None:
        prev=cur
        cur=cur.next
        if(prev.val==cur.val):
            delNode=cur
            prev.next=cur
            del delNode
    return head        