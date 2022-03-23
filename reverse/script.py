
emptyList = []

number = int(input('How many number do you want to enter?'))
print("\n")


for i in range(0,number):
    print('what is your number',i+1,'?')
    num = int(input())
    #num = int(input('What is your number ? '))
    emptyList.append(num)


#emptyList.reverse()

emptyList.reverse()


print(emptyList)




exit() 

