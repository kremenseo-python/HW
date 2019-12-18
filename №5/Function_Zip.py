# понять, как работает функция zip


international = ("xs", "s", "m", "l", "xl", "xxl")
usa = (46, 48, 50, 52, 52, 54)
all = list(zip(international, usa))
print(all)
all2 = dict(zip(international, usa))
print(all2)