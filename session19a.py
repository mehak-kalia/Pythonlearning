def my_random_generator( ):
    import datetime
    from time import sleep
    l = []
    tym = []

    n = int(input("Enter the no. of numbers to be generated"))

    for i in range(n):
        time = datetime.datetime.now()
    t = time.microsecond

    l.append(t)
    sleep(0.012)

    print(l)

    for i in (l):
        tym.append(i / 10000)

    print(tym)

def main():
    my_random_generator()

if __name__ == '__main__':
    main()