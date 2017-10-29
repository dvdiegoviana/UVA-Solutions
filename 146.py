def sort(arr):
    if(len(arr)<=1):
        return arr
    pivot = arr[0]
    pivotArr = [pivot]
    lessArr = []
    bigArr = []
    for i in range(1,len(arr)):
        if(arr[i]>pivot):
            bigArr.append(arr[i])
        elif(arr[i]<pivot):
            lessArr.append(arr[i])
        else:
            pivotArr.append(arr[i])
    lessArr = sort(lessArr)
    bigArr = sort(bigArr)
    return lessArr+pivotArr+bigArr



def getNext(arr): 
    if(len(arr)==1):
        return False
    next = getNext(arr[1:len(arr)])
    if(next==False):
        minPos = getMinPosBiggerThanFirst(arr)
        if(minPos==0):
            return False
        aux = arr[0]
        arr[0] = arr[minPos]
        arr[minPos] = aux
        return [arr[0]] + sort(arr[1:len(arr)])
    else:
        return [arr[0]]+next

def getMinPosBiggerThanFirst(arr):
    min = arr[0]
    minPos = 0
    for i in range(len(arr)):
        if(minPos==0 and arr[i]>arr[0]):
            minPos=i
            min = arr[i]
        if(arr[i]<min and arr[i]>arr[0]):
            min = arr[i]
            minPos = i
    return minPos
    

while(1):
    code = input()
    if(code == "#"):
        break
    nextCodeArr = getNext(list(code))
    if(nextCodeArr==False):
        print("No Successor")
    else:
        print(''.join(nextCodeArr))