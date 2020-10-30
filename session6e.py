a = 10

"""def square():
    a = 12
    result = a*a
    print("[square]square of {} with {} is: {}".format(a, a,  result))"""
def square():
    global a #this globalises a to out of the function
    a = 12
    result = a*a
    print("[square]square of {} with {} is: {}".format(a, a,  result))


square()
print("a =", a)
print("this staetement belongs to main")
result = a*a
print("[main] square of {} with {} is: {}".format(a, a, result))
