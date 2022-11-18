n = input("enter the string\n")


def al(n):
    if n.isalpha():
        print("true")
    else:
        print("false")


def cv(n):
    v = 0
    c = 0
    n.lower()
    for i in n:
        if(cv == 'a' or cv == 'e' or cv == 'i' or cv == 'o' or cv == 'u'):
            v = v+1
        else:
            c = c+1
    print("the num of vowels", v)
    print("the num of const", c)


def pal(n):
    if(n == n[::-1]):
        print("The  Sting is palin")
    else:
        print("Is not a palin")


def freq(n):
    fre = {}

    for i in n:
        if i in fre:
            fre[i] += 1
        else:
            fre[i] = 1

    print("the frequency of chatecters is " + str(fre))


def num(n):
    dig = 0
    if n.isdigit():
        dig = dig+1
        print("digits = ", dig)
    else:
        print("nodigit present")


def word(n):
    con = len(n.split())
    if con > 1:
        print("it is a ", con, " word sentence")
    else:
        print("it is a word")


al(n)
cv(n)
pal(n)
num(n)
freq(n)
word(n)
