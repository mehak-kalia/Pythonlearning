restaraunt=('john\'s coffee shop') #in single colon use escape sequences to differentiate appsotrophie

restaraunt= (r"john\'s coffee shop") #when we write r aside it becomes a raw string no sequences work

print(restaraunt)
#\ only breaks code and not the output
message = "we are learing python" \
    "it is an awesome day" \
    "lets code"

print(message)

#to break the message without escape use triple codes

my_messages = """we are learing python
it is an awesome day
lets code"""

print(my_messages)
