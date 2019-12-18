f = open('numbers.txt', 'r')

b = [line.strip() for line in f]
print(b)

fizz = int(input())
buzz = int(input())
a = map(int, b)

result = []
results = result
for i in a:
    if ((i % fizz == 0) and (i % buzz == 0)):
        result.append('FB')
    elif i % fizz == 0:
        result.append('F')
    elif i % buzz == 0:
        result.append('B')
    else:
        result.append(i)

print(results)
f = open("result.txt", 'w')
for i in results:
    f.write("%s\n" % i)