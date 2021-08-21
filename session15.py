"""pesistance ; filr handling concepts"""

class User:
    def __init__(self):
        self.name = input("enter your name")
        self.phone = input("enter your phone no.")
        self.email = input("enter your email")
    def show(self):
        print("your details are :\n {} | {} | {}".format(self.name, self.phone, self.email))
    def RegisterUser(self):
        #file = open("data.csv", "w") #w over writes the new data
        file = open("data.csv", "a") # adds data

        data = "\n {} | {} |{}".format(self.name, self.phone, self.email)
        file.write(data)
        file.close()

def main():
    uref = User()
    uref.show()
    uref.RegisterUser()
if __name__ == '__main__':
    main()
