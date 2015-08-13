n = int(input('Введите количество программистов[0..1000]: '))
p1 = str('программист')
p2 = str('программиста')
p3 = str('программистов')
if len(str(n)) == 1:
    if n == 1:
        print (n, p1)
    elif n == 2 or n == 4 or n ==3:
        print (n, p2)
    else:
        print (n, p3)
        
elif len(str(n)) == 2:
    if n%10 == 1:
        print (n, p1)
    elif n%10 == 2 or n%10 == 4 or n%10 ==3:
        print (n, p2)
    else:
        print (n, p3)

elif len(str(n)) == 3:
    if n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14:
        print (n, p3)
    elif (n%100)%10 == 1:
        print (n, p1)
    elif (n%100)%10 == 2 or (n%100)%10 == 4 or (n%100)%10 ==3:
        print (n, p2)
    else:
        print (n, p3)
elif n == 1000:
    print (n, p3)
