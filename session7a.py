a = 10
b = a

a = 11

print(a,b)
print(id(a))
print(id(b))

numbers1 = [10, 20 ,30]
numbers2 = [10, 20, 30]
print(id(numbers1))
print(id(numbers2))
print(id(numbers1[0]))
print(id(numbers2[0]))