students = ["john", "fionna", "dave"]
print(students, type(students))

#concatenation

morestudents = students + ["raju", "mohan"]
print(students)
print(morestudents)
#repetition

repeatedstudents = students * 2
print(repeatedstudents)
print(students)

#membership testing

print("john" in students)
print("lola"  in students)

#indexing

print(students[0])
print(students[len(students) - 2])
print(students[-1])

#slicicng

print(students[0:1])
print(students[1:])