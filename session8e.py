#conversion

numbers1 = (10, 20, 30, 40, 50, 20, 10)
print(numbers1, type(numbers1), id(numbers1), len(numbers1))
#tuple to list is not a modification but creation of a new list in memory
numbers2 = list(numbers1)
print(numbers2, type(numbers2), id(numbers2), len(numbers2))

numbers3 = set(numbers1)
print(numbers3, type(numbers3), id(numbers3), len(numbers3))

#numbers4 = dict(numbers1)
#print(numbers4, type(numbers4), id(numbers4), len(numbers4))
#diction conversion not possible as it works on key value pair


