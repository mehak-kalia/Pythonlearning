lref1 = lambda amount: amount - amount*(0.20)

product_prices = [1000, 2000, 3000, 4000]

for prices in product_prices:
    print(lref1(prices))

result = map(lref1, product_prices)
print(result, type(result))

print(list(map(lambda num: num/2, product_prices)))

numbers = list(range(10,21))
print(numbers)

l1 = list(map(lambda num:num%2 == 0, numbers))
l2 = list(map(lambda num:num%2 != 0, numbers))
print(l1 ,l2)

l3 = list(filter(lambda num:num%2 == 0, numbers))
l4 = list(filter(lambda num:num%2 != 0, numbers))
print(l3, l4)

