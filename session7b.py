#pass by reference

def square(number):
    print("hashcode of number is", id(number))
    for i in range(0, len(number)):
        number[i] = number[i] * number[i]
    print("hashcode of no. now is", id(number), number)
    print(id(number[0]))

def main():
    nums = [10, 20, 30]
    print(id(nums[0]))
    print("hashcode of num and num is", id(nums), nums)
    square(nums)
    print(" after id of num is", id(nums), nums)


main()
