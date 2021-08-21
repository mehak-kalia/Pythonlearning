
print("this is session18")
print("session 18 __name__ is", __name__)
name = "john watson"

def add(num1, num2):
    result = num1+num2
    print("result is :", result)

class User:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        print("user object created")

    def show(self):
        print("details of the user are {} | {} | {} | {}".format(self.name, self.phone, self.email, __name__))

def main():

    print("this is session18")
    print("session 18 __name__ is", __name__)
    add(10, 20)
    uref = User("fin", 291209021, "fin@")
    uref.show()

if __name__ == '__main__':
    main()