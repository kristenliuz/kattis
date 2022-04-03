

start = 7
upperlimit = 10
lowerlimit = 0

num = int(input())
#3
for i in range((num)):
   
    request = input()
    if request == 'Skru op!':

        start += 1
        if start > upperlimit:
            start -=1
    else:

        start -= 1
        if start < lowerlimit:
            start +=1   
    

print(start)

        
