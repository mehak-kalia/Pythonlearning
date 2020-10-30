
"""print("while loop")
i=1

while i<=10:
    print("i is", i)
   #i += 1
    i += 2

print("nested loop")
#for i in range(1,11):
for i in range(1,11,2):
        print(" i is:", i)

#nested loops
for i in range(1,6):
    print(" >> i is:", i)

    for j in range(1,4):
        print(j, end=" ")

print()

#break and continue
print("break and continue")
print("break")
my_floor = 5
total_floor = 10
start = 1
for floor in range(start, total_floor+1):
    print("floor#", floor)
    if floor == my_floor:
        print("________________________")
        print("my floor has arrived", my_floor)
        print("________________________")
        break #terminates the loop"""


i=1
for i in range(1, 11):
    if i > 5:

      print("i is", i)

      print("{} * {} = {}".format(5, i, (5 * i)))
      