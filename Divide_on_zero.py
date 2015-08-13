a = int(input("Input A: "))
b = int(input("Input B: "))
if b != 0:
    print(a/b)
else:
    print("It's impossible to divide on zero")
    b = int(input("Input nozero B: "))
    if b == 0:
        print("Reinput zero is not a way to solve the problem."
              "Attempt failed")
    else: print(a/b)
