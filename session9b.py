name = "Mehak Kalia"
upper_name = name.upper()
print("name is:", name)
print("name in upper case is:", upper_name)

print(name.capitalize())

names = "john, jennie, jim, sam"
print(names[0])
print(names[(len(names))-1])

print(names.index("h"))
print(names.index(" "))

print(names.split(), type(names.split()))

print(names.replace('j', 'k'))
print(names.count("j", 0 , len(names)))

quote = "live life king size"

for i in range(0, len(quote)):
    print(quote[i], end = " ")

number = "100"
print(number.isdigit())