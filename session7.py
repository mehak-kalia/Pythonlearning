def sayhello(name):
    print("my names is {}".format(name))

sayhello("john")

print("sayhello is :", sayhello)
#reference copy
hello = sayhello

print(hello)
