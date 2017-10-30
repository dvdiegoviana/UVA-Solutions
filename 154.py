def incrementBinCount(binColor,binType):
        getCount(binColor)[binType]+=1

def getCount(binColor):
    if(binColor=='r'):
        return countR
    elif(binColor=='o'):
        return countO
    elif(binColor=='y'):
        return countY
    elif(binColor=='g'):
        return countG
    elif(binColor=='b'):
        return countB

def getConvergenceCount(bin):
    total = 0
    total += countR[bin['r']]
    total += countO[bin['o']]
    total += countY[bin['y']]
    total += countG[bin['g']]
    total += countB[bin['b']]
    return total







countR = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
countO = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
countY = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
countG = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
countB = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
endProgram = False

while(True):
    countR = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
    countO = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
    countY = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
    countG = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
    countB = {'P':0,'G':0,'S':0, 'N':0, 'A':0}
    binDic = []


    lines = []
    while(True):
        line = input()
        if(line[0]=='e' or line[0]=='E'):
            break
        elif(line=='#'):
            endProgram=True
            break
        else:
            lines.append(line)
    
    if(endProgram):
        break
    

    for i in range(len(lines)):
        line = lines[i]
        binDic.append({})
        binDic[i][line[0]]=line[2]
        incrementBinCount(line[0],line[2])
        binDic[i][line[4]]=line[6]
        incrementBinCount(line[4],line[6])
        binDic[i][line[8]]=line[10]
        incrementBinCount(line[8],line[10])
        binDic[i][line[12]]=line[14]
        incrementBinCount(line[12],line[14])
        binDic[i][line[16]]=line[18]
        incrementBinCount(line[16],line[18])


    leastImpact = 0
    leastImpactIndex = -1

    for i in range(len(binDic)):
        convergenceCount=getConvergenceCount(binDic[i])
        if(convergenceCount>leastImpact):
            leastImpact=convergenceCount
            leastImpactIndex=i
    print(leastImpactIndex+1)
