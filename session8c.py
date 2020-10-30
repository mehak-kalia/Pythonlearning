ids ={"john.w", "dave.h", "fionna", "rishi"}
print(ids, type(ids), id(ids))

#since it is a set no hashing or slicing

# i set we needd to itterate in order to access elements

#for i in range(o, len(ids)):
 #   print(ids[i]) error so in sets enhanced for loop is used

for id in ids:
     print(id)
#in case of strings max and min works using ascii code comparison but only for th firsr charracter
print(len(ids))
print(max(ids))
print(min(ids))