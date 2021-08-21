import datetime as dt

class Fee:

    def __init__(self, rollNum=0, amount=0):
        self.rollNum = rollNum
        self.amount = amount
        self.datetime = dt.datetime.today()


    def show_fee(self):
        print("{} | {} | {}".format(self.rollNum, self.amount, self.datetime))

    #def add(self, fee):
     #   temp = Fee()
      #  temp.amount = self.amount + fee.amount
       # return temp
    def __add__(self, fee):
        temp = Fee()
        temp.amount = self.amount + fee.amount
        return temp

    def __copy__(self):
        print("DEEP COPY")
        temp = Fee(self.rollNum, self.amount)
        temp.datetime = self.datetime
        return temp


def main():
    fref1 = Fee(101, 2000)
    fref2 = Fee(102, 2000)
    fref3 = Fee(103, 2000)

    #totalfeeref = fref1.add(fref2.add(fref3))
    #print(totalfeeref.amount)

    totalfeeref = fref1 + fref2 + fref3
    print(totalfeeref.amount)

    # fRef1 and my_fee both points to the same memory location
    # my_fee = fRef1 # Shallow Copy as we juts make 2 references pointing to the same object with same data

    my_fee = fref1.__copy__()  # Deep Copy Operation where, 2 References points to 2 different objects and may or may not share the same data later but initially it would be same
    print(fref1)
    print(my_fee)

    print(fref1.__dict__)
    print(my_fee.__dict__)


if __name__ == '__main__':
    main()