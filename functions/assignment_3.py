# logical operations
age= input("Enter your age:")
age= int(age)           #this is neccesary beacuse operators >= only support integars
if (age >= 20):
    print("You are an adult")
else:
    print("You are still young", "\n")

#comparison operations
set1= ['John', 'Mary', 'Sarah']
set2= ['John', 'Sarah', 'Mark']
print(set1==set2, "\n")

def interest():
    p= input("Enter the priciple amount: ")
    p= int(p)
    r= input("Enter the rate: ")
    r= int(r)
    t= input("Enter the number of years:")
    t= int(t)

    interest1= (p*r*t)/100
    print("The total interest is: ",interest1)

    if (interest1 >100000):
        print("You have earned a large amount")
    else:
        print("You have earned little interest", "\n")
interest() 

#assignment operators

a= input("Enter any number: ")
b= input("Enter the exponent value:")

a=int(a)
b=int(b)

a**=b
print("The answer for 'a' is: ", a)

