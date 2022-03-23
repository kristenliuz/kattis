
emptyList = []

#umber = int(input('How many number do you want to enter?'))
number = int(input())

for i in range(0,number):
    #print('what is your number',i+1,'?')
    num = int(input())
    #num = int(input('What is your number ? '))
    emptyList.append(num)


#emptyList.reverse()

emptyList.reverse()


#print(emptyList)
for i in emptyList:
    print(i)



exit() 

