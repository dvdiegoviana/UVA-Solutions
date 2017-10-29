import re

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

def checkAnagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if(len(word1)!=len(word2)):
        return False
    word1 = ''.join(sort(list(word1)))
    word2 = ''.join(sort(list(word2)))
    if(word1==word2):
        return True
    else:
        return False
    



words = []
anagrams = []
ananagrams = []

while(True):
    line = input()
    if(line=="#"):
        break
    #line = "ladder came tape soon leader acme RIDE lone Dreis peat ScAlE orb eye Rides dealer      NotE derail LaCeS drIed noel dire Disk mace Rob dries"
    line = re.sub(' +',' ',line)
    words = words + line.split(' ')

i = 0
while(len(words)>0):
    isAnagram = False
    word = words[i]
    words.remove(words[i])
    if(len(word)>1):
        for wordToTest in words:
            if(checkAnagram(word,wordToTest)):
                isAnagram=True
                words.remove(wordToTest)
    if(isAnagram!=True):
        ananagrams.append(word)

ananagrams = sort(ananagrams)

for ananagram in ananagrams:
    print(ananagram)



