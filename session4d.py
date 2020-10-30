#case study of promo codes
amount = int(input("enter amount value:"))

if amount >= 149:
    print("elidgible to apply the promo code")

else: print("not elidgible to apply the promo code")

# Nested if/else | if/else within the if/else

if amount >= 149:
    print("Eligible to Apply Promo Code")
    print("Apply CRAVINGS to get 40% Off Upto \u20b9100")
    promoCode = input("Enter the Promo Code: ")
    if promoCode == "CRAVINGS":
        discount = 0.40 * amount
        if discount >= 100:
            discount = amount - discount
        amountToPay = amount - discount
        print("Discount of \u20b9", discount, "applied. Please Pay: \u20b9", amountToPay)
    else:
        print("Sorry !! Promo Code Not Applicable")
        print("Please Pay: \u20b9", amount)
else:
    print("Not Eligible to Apply Promo Code")


# CRAVINGS: 40% Off upto Rs 100 | amount >=149
# JUMBO:    50% Off upto Rs 200 | amount >=500
# BINGO:    Flat 20% Off        | amount >=100