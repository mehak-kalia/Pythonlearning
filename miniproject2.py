print("~~~~~~~~~~~~~~~~~~~The Table By Basant~~~~~~~~~~~~~~~~~~~~~")
import pprint

RESTAURANT = {"name": "The Table By Basant",
              "Reviews": 4.1,
              "Reviewed by": "113.8k customers",
              "specialisation": "north indian , pizza , burger etc.",
              "promo codes": ("GOBIG", "CRAVINGS", "ZOMATO")

              }
print(RESTAURANT)
print()
print()
print("~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~")
A = {"dal": 120,
            "cheese tomato": 130,
            "mixed vegtables": 90,
            "veg pulao": 120}


print("lunch and dinner:\n", A)

B={"idli": 50,
            "vada": 70,
            "masala dosa": 110,
            "coconut chutney": 30}


print("south indian:\n", B)

C={ "pizza": 200,
            "burger": 80,
            "pasta": 160,
            "fries": 70}


print("snacks:\n", C)

D={ "shake": 100,
            "pepsi": 40,
            "gulaab jamun ": 25,
            "rasgulla": 20}


print("sweets and beverages:\n", D)

menu = [A, B, C, D]

print("~~~~~~~~~~~~~~~~~~~~LETS START BUILDING YOUR CART~~~~~~~~~~~~~~~~~~~~~~~~")
cart = []
choice = "yes"

