fizz = int(input())
buzz = int(input())
i = int(input())

for i in range (1, ++i):

    if ((i % fizz == 0) and (i % buzz == 0)):
        print ("FB")

    elif i % fizz == 0:
        print ("F")
    elif i % buzz == 0:
         print ("B")

    else:
        print (i)

