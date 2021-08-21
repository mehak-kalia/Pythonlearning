lref1 = lambda radius = 1.0 : 3.14*float(radius)*float(radius)
print(lref1(2))

lref2 = lambda x,y : x**y
print(lref2(2,3))

lref4 = lambda x = input("enter x"), y = input("enter y"): lref1(x) + lref2(x,y)
print(lref4())