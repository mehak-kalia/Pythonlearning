#bitwise and shift operators

num1 = 10
num2 = 2
print(bin(num1)) # 1010
print(bin(num2)) # 0010

num3 = num1 & num2

print(bin(num3)) # 0010
print(num3)

num4 = num1 | num2
print(bin(num4
        ))

num5 = num1 ^ num2 #ex or
print(bin(num5)) #same value flse opposite value true

num6 = num1 >>2

print(bin(num6))

# n >> x means integral divide n by 2 power x
# n >> x means integral multiplication n by 2 power x

num7 = num1 <<3
# 1010---  -> 1010000

print(bin(num7))

num8 = -12
print(bin(num8))

num9 = num8 >>3
print(bin(num9))
print(num9)