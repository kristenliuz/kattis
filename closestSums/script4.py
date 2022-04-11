
def doOneSet():
    maxInput = int(input())
    numList = []
    sumList = []
    for j in range(maxInput):
        enter = int(input())
        numList.append(enter)
        #numList.append(enter)

    maxSum = int(input())
    for k in range(maxSum):
        enterSum = int(input())
        sumList.append(enterSum)
    print(numList, sumList)   
    
    print('TRANSFORM : ')
    print('numList: ',numList)
    addList3 = []
    a = 1
    b = 0
    for place, value in enumerate (numList):
        if place >= a:  
            print(value)
            w = numList[b] + value
            addList3.append(w)
            print(addList3)
    
        a +=1
        b +=1
    print(addList3)

doOneSet()
#doOneSet()
#doOneSet()

exit(0)


'''





print('TRANSFORM : ')

####################
print('Case 1:')
addList3 = []

a = 1
b = 0
while (4>a >0):

    for place, value in enumerate (numlist):
        if place >= a:  
            w = numlist[b] + value
            addList3.append(w)

    a +=1
    b +=1
print('addList3 : ',addList3)

c=0
while (c <3):

    diff2= []

    for i in addList3:
        diff = abs(i - sumList[c])
        diff2.append(diff)
 

    print('diff2 : ',diff2)

    pair = list(zip(addList3,diff2))

    print(pair)
    minimum = min(map(lambda elem: elem[1], pair))

    for elem in pair:
        if elem[1] == minimum:
            print(elem[0])
            print('-------------Closest sum to ',sumList[c],'is ', elem[0])

    c +=1


'''


