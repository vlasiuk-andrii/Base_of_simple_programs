a = int(input('Insert a: '))
b = int(input('Insert b: '))
d = 0
if a == 0 or b ==0:
    print('Zero values are not allowed')
else:    
    while 1:
        d+=1
        if (d%a == 0) and (d%b == 0):
            print('Minimal mehrere=', d)
            break

