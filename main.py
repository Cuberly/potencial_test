s = int(input())
a = input()
a = a.replace("→", " <= ")
a = a.replace("∧", " and ")
a = a.replace("∨", " or ")
a = a.replace("\/", " or ")
a = a.replace("¬", " not ")
a = a.replace("≡", " == ")
if s == 4:
    print("x y z w /")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    if not eval(a):
                        print(x, y, z, w, 0)
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    if eval(a):
                        print(x, y, z, w, 1)
elif s == 3:
    print("x y z /")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not eval(a):
                    print(x, y, z, 0)
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not eval(a):
                    print(x, y, z, 1)
