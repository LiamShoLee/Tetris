

#read in file to tempTuple
#read in only name and score

scores = [line.strip('\n') 
    for line in open('scores.txt', 'r').readlines()]
tempTuple = ("Player1", 10000)

#insert templist as an element of fulllist
#repeat for 10

fullList = []


#insert new score into fulllist

#sort list

for x in fullList:
    if fullList[x][3] > fullList[x-1][3]:
        tempTuple = fullList[x-1][3]
        fullList[x][3] = 

#reprint fulllist into file
