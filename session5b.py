"bubble sort"

prices = [1200, 8800, 1290, 1900, 1750]
print("prices aree:")
print(prices)
n = len(prices) # n = 5
for i in range(0, len(prices)):
    for j in range(0, (len(prices)-i - 1)):
        if prices[j] > prices[j+1]:
            prices[j], prices[j+1] = prices[j+1], prices[j]


print("prices now aree")
print(prices)