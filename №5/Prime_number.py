# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map
a = int(input())

k = 0
# пробегаем все числа от 2 до N
for i in xrange(2, n+1):
    # пробегаем все числа от 2 до текущего
    for j in xrange(2, i):
        # ищем количество делителей
        if i % j == 0:
            k = k + 1


#НЕ ОКОНЧИЛ