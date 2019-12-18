print ("- Do you want go to restaraunt?\n- If i have a lot of money - i will go\n- How much money do you have?")
money = int(input())
if ((money >= 500) and (money <= 1000)):
	print ("You have a lot of, let's go in best restaraunt")
elif ((money <= 500) and (money >=100)):
	print ("- Good, we can eat in fastfood")
else:
        print ("Ohh, it's to little, maybe next time") 
