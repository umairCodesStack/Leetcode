def recoverOrder(order, friends):
    sortedFriends=[]
    i=0
    for x in order:
        if x in friends:
            sortedFriends.append(x)
    return sortedFriends


print(recoverOrder([1,4,5,3,2], [2,5]))
#print(recoverOrder([3,1,2,5,4], [1,3,4]))
