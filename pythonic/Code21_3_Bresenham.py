print("Point A:")
print("Enter x1: ")
x1 = input()
x1 = int(x1)
print("Enter y1: ")
y1 = input()
y1 = int(y1)

print("Point B:")
print("Enter x2: ")
x2 = input()
x2 = int(x2)
print("Enter y2: ")
y2 = input()
y2 = int(y2)

# initialize needed values
deltaX = x2-x1
deltaY = y2-y1
twoDeltaX = 2 * deltaX
twoDeltaY = 2 * deltaY

# r initial
r0 = twoDeltaY - deltaX
r = []
r.append(r0)

print("\nDelta X:")
print(deltaX)
print("\nDelta Y:")
print(deltaY)

if deltaX > deltaY:
    # for x-coordinates
    x = []
    if x1 < x2:
        for incX in range(x1, x2+1):
            x.append(incX)
        print("\nX-coordinates:")
        print(x)
    else:
        for decX in range(x1, x2-1, -1):
            x.append(decX)
        print("\nX-coordinates:")
        print(x)

    # for r and y-coordinates
    for i in r:
        while len(r) != len(x):
            if i > 0:
                i = i + (twoDeltaY - twoDeltaX)
                r.append(i)
                y = []
                y.append(y1)
                for incY in y:
                    while len(r)-1 != len(y):
                        incY = y1 + 1
                        y.append(incY)
                y.append(y2)  
            else:
                i = i + twoDeltaY
                r.append(i)
                y = []
                y.append(y1)
                for incY in y:
                    while len(r)-1 != len(y):
                        incY = y1 + 0
                        y.append(incY)
                y.append(y2) 
    print("\nY-coordinates:")
    print(y)
else:
    # for r and x-coordinates
    for i in r:
        while len(r) != len(x)+1:
            if i > 0:
                i = i + (twoDeltaY - twoDeltaX)
                r.append(i)
                x = []
                x.append(x1)
                for incX in x:
                    while len(r) != len(x):
                        incX = x1 + 1
                        x.append(incX)
                x.append(x2)  
            else:
                i = i + twoDeltaY
                r.append(i)
                x = []
                x.append(x1)
                for incX in x:
                    while len(r) != len(x):
                        incX = x1 + 0
                        x.append(incX)
                x.append(x2) 
    print("\nY-coordinates:")
    print(x)
         # for y-coordinates
    y = []
    if y1 < y2:
        for incY in range(y1, y2+1):
            y.append(incY)
        print(y)
    else:
        for decY in range(y1, y2-1, -1):
            y.append(decY)
        print(y)
    













