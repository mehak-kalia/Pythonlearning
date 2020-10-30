#conditional operators
# == != <> <= >=

#logical operators and or
#membership operators is not is

cabfare = 100
wallet = 70

print("can i book a cab", (cabfare <= wallet))

username = "john.username@gmail.com"
password = "john123"
print("user authentication 1", (username == "john.username@gmail.com"))
print("user authentication 2", (password == "john123"))

print("user authentication for login", (username == "john.username@gmail.com") and (password == "john123"))

otp = 3057
user_otp = int(input("enter the otp"))

print("otp matched!!", (user_otp == otp))

#boolean

isinterneton = False
print("can i login?", isinterneton, type(isinterneton))

name = "fionna"
print(name is "fionna")
print(name == "fionna")

# as of noe is ==

print(name is not "john")