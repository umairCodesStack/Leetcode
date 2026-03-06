def finalValueAfterOperations(operations):
    init=0
    for x in operations:
        if x == "--X" or x == "X--":
            init=init-1
        else:
            init=init +1
    return init
print(finalValueAfterOperations(  ["X++","++X","--X","X--"]))
def findWordsContaining(words, x):
    indecies=[i for i in range(len(words)) if x in words[i] ]
    return indecies
print(findWordsContaining(["leet","code"],"e"))

