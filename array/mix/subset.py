import itertools


def getSubsets(arr):
    subsets = []
    for i in range(len(arr)+1):
        for comb in itertools.combinations(arr, i):
            subsets.append(list(comb)) 
    return subsets

print(getSubsets([5,1,6]))

def generateSubsets(arr):
    subsets=[]