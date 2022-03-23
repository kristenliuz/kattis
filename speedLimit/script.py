#https://open.kattis.com/problems/speedlimit


test = [20, 2, 30, 4, 50,7]

mileHour = (test[1::2])
numberOfTime = (test[0::2]) 

print(mileHour)
print(numberOfTime)

mileHour2 = []
mileHour2.append(mileHour[0])
for x, y in zip(mileHour,mileHour[1:]):
    print(x)
    print(y)
    mileHour2.append(y-x)
print(mileHour2)


total =[]

for a, b in zip(mileHour2,numberOfTime):
    total.append(a*b)

print(total)


print('difficult')
test2 = [2, [20, 2, 30, 4], 2, [20, 1, 50, 3]]



exit(0)





total =[]

for a, b in zip(mileHour,numberOfTime):
    total.append(a*b)

print(total)
exit()

test = [2, [20, 2, 30, 4], 2, [20, 1, 50, 3]]

print(test)

mileHour = (test[1::2])
numberOfTime = (test[0::2]) 

print(numberOfTime)

print(mileHour)

for i in mileHour:
    print('check lopp')
    print(i)
    for mile in i[0::2]:
        print('mile')
        print(mile)
        #for mile in i[0::2]:
            #print(mile)

exit()


num = int(input("How many inputs? "))
if num == -1:
    exit(0)

mmm=1
mother_empty = []
empty = []

while mmm <= num:
    mile=int(input("miles "))
    #print(mile)
    hour = int(input("hours "))
    empty.append(mile)
    empty.append(hour)
    mmm+=1

print(empty)  

mother_empty.append(num)
mother_empty.append(empty)
print(mother_empty)  

num = int(input("How many inputs? "))
if num == -1:
    exit(0)

mmm=1

while mmm <= num:
    mile=int(input("miles "))
    #print(mile)
    hour = int(input("hours "))
    empty.append(mile)
    empty.append(hour)
    mmm+=1

print(empty)  

mother_empty.append(num)
mother_empty.append(empty)
print(mother_empty)  








exit(0)




'''

with open('inputValue.txt') as topo_file:
    lines=topo_file.readlines()
    a = len(lines)
    print("lines",a)


    empty = []
    for line in lines:
        print(line)
        empty.append(line)
    
    print(empty)



    empty2 = [elem.strip().split('\n') for elem in empty]
    print(empty2)




#exit(0)






#slow performance
with open('inputValue.txt') as topo_file:
    a = len(topo_file.readlines())

with open('inputValue.txt') as topo_file:  
    for line in topo_file:
        print (line)  # The comma to suppress the extra new line char
    
'''




