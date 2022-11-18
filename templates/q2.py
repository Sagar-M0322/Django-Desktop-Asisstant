n = int(input("enter the num"))


def oe(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


def prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if(n % i) == 0:
                print("is not prime", n)
                break
        else:
            print("is a prime", n)
    else:
        print("not a prime", n)


def ly(n):
    if((n % 400 == 0) or ((n % 4 == 0)) and (n % 100 != 0)):
        print("Is a leap year ", n)
    else:
        print("not a leap year ", n)


def count(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    print("num of digits are "+str(count))


def ny(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    if (count == 4):
        print("a year")
    else:
        print("a not year")


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact


fff = factorial(n)


def fact(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    if count < 3:
        print("factorial of is", fff)
    else:
        print("Number is more than two digits ")


count(n)
ly(n)
prime(n)
oe(n)
ny(n)
fact(n)
