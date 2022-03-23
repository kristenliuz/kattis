


def kristenFunction ():
    print('Print Kristen Function')

kristenFunction()


def apple():
    print('print apple apple')

apple()



def fruit (color):
    print('This fruit is ', color)


fruit('red')

exit()
num = int(input())
while num > 0:
    print('run')






'''
num = int(input())
while num > 0:
     dist = 0
     lasth = 0
     while num:
         speed, hour = map(int, input().split())
         hour -= lasth
         dist += speed * hour
         lasth = hour
         num -= 1
     print(dist)
     num = int(input())


'''





'''

# Read one number that describes number of speed/hour inputs
num = int(input())

# Do while number input is over 0 (that is -1 exits)
while num > 0:
     # Start with distance to zero
     dist = 0
     # Start with no hours from last input
     lasth = 0

     # Loop while num is greater then 0
     while num:
         # Read one string with two values
         # Split into a list of values
         # Map them with int() to create integers
         # Save first as speed and second as hour
         speed, hour = map(int, input().split())

         # Remove last hour input
         hour -= lasth

         # Add new distance
         dist += speed * hour

         # Save last hour input
         lasth = hour

         # Decrease number
         num -= 1

     # Print resulting dist
     print(dist)

     # Reread one first number
     num = int(input())




num = int(input())
while num > 0:
     dist = 0
     lasth = 0
     while num:
         speed, hour = map(int, input().split())
         hour -= lasth
         dist += speed * hour
         lasth = hour
         num -= 1
     print(dist)
     num = int(input())
     
'''
