
import re
import sys
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
email = "this is my mail id sagar@gmail.com"


def domain(email):
    print("The original string is : " + str(email))
    res = email[email.index('@') + 1:]

    print("The extracted domain name : " + str(res))


def vali(email):
    count1 = 0
    for a in email:
        if (a.isupper()) == True:
            count1 += 1

        if(re.fullmatch(regex, a)):
            print("valid email id")

    if(regex.search(email) != None):
        print("speciacharecters present")
    else:
        print("No special charecters")

    if(count1 <= 0):
        print("no upper case please include for better emailid")
    if(re.fullmatch(regex, email)):
        print("valid emailid")

    lst = re.findall('\S+@\S+', email)
    print("emails id in the given string is", lst)


domain(email)
vali(email)

file_path = 'C:/Users/Sagar/AppData/Local/Programs/Python/Python39/randomfile.txt'
sys.stdout = open(file_path, "w")
print(domain(email))
print(vali(email))
