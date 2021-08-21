menu = { 101: 20, #samosa
         201 : 100, #tikki
         301: 130, #noodles
         401: 160, #burger
         501: 200}


class Order:

    order_id = 0

    def __init__(self):
        Order.order_id += 1
        self.oid = Order.order_id
        self.customer_name = input("enter your name :")
        self.customer_phone = input("enter your phone :")

        self.order_items = []
        choice = "yes"
        while choice == "yes":
            id = int(input("enter id of the items:"))
            self.order_items.append("{} : {}".format( id , menu[id]))
            choice = input("would you like to add more items yes/no?:")

    def show_order(self):
        print( "{} | {} | {}" .format(self.oid, self.customer_name, self.customer_phone))
        print()
        print("your order is : \n", self.order_items)


    def save_order(self):
        file = open("data.csv", "a")
        data = "{} | {} | {} | {} \n".format(self.oid, self.customer_name, self.customer_phone, self.order_items)
        file.write(data)
        file.close()
        print("details saved!")

    @staticmethod
    def read_order():
        file = open("data.csv", "r")
        lines = file.readlines()
        for line in lines:
            print(line)
        data = line.split(",")
        for i in range(0, len(data)):
              print(data[i], end = " ")
def main():
    """order = Order()
    choice = "yes"
    while choice == "yes":

      order.show_order()
      order.save_order()
      choice = input("would you like to add another order yes/no?:")"""

    Order.read_order()

if __name__ == '__main__':
    main()
