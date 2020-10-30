#list comprehension ( editing in list only instead of making a special function)
product_prices=[1000, 2000, 5000, 4400, 8000]

print([0.5 *x for x in product_prices])

print([0.4 *x for x in product_prices if x <= 5000])
print([0.6 * x for x in product_prices if x>5000])

