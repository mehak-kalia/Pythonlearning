name = "john.watson"
print(name, type(name), len(name), id(name))

another_name = "john.watson"
print(another_name, type(another_name), len(another_name), id(another_name))
# name and another name point to same data so hashcode is also same

print(len(name))

phone= input("enter urr phone number!")
if len(phone) == 15:
    print("thanks for enetring urr phone no. is:", phone)

else:

    phone = input("enter urr phone number!")