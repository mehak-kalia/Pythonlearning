employee = {"name": "John",
            "age": 24,
            "email": "john.watson@gmail.com",
            "phone": 9216559059}
print(employee, len(employee), type(employee), id(employee))
print(max(employee))
print(min(employee))

print(list(employee.keys()))
print(employee.values())

for attribute in employee:
    print(attribute)

for attribute_values in employee.values():
    print(attribute_values)
tuple_employee = tuple(employee.items())
for items in tuple_employee:
    print(items)