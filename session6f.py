# recursion : function executing itself again and sgain

for i in range (1, 11):
    print("i is", i)

# function can also create same effect as that of loops through recursion

def printnumber(number):
    if number > 10:
        return
    print("number is :", number)
    number += 1
    printnumber(number)
    if number >=10:
        return

printnumber(1)
