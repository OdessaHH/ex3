# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn



"""1"""
"""
for i in range(0,3):
    a = int(input("enter number: "))
    if a % 2 == 0:
        print("even number")
    else: print("odd number")
"""


"""2"""



"""
while True:
    i = int(input("Please enter a number between 1 to 3 or '0' to end program: "))
    if i == 0:
        print("Bye bye!")
        break
    elif i == 1:
        j = int(input("Please enter the range number: "))
        for x in range(1,j+1):
            print(x)
    elif i == 2:
        k = int(input("Please enter starting number: "))
        l = int(input("Please enter stopping number: "))
        for y in range(k, l+1):
            print(y)
    elif i == 3:
        m = int(input("Please enter starting number: "))
        n = int(input("Please enter stopping number: "))
        o = int(input("Please enter step: "))
        for z in range(m, n+1, o):
            print(z)
    else:
        print("sorry, but you have to choose numbers between 1, 2 or 3! or '0' to end this.")

"""



















"""3"""

"""
Alex
numb = int(input("enter a number: "))
print("dividers:",numb, end = " ")
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        print(i, end = " ")
"""


"""Peer
print("")
print("Task3")
print("")
user_number = int(input("Enter a number: "))
for i in range(user_number+1, 1, -1):
    if user_number % i == 0:
        print (i)
"""

""" #Nadia
x= int(input('number'))
for i in range(1,x+1):
if x % i== 0 :
print(i) 
"""




"""4"""





"""

num = int(input("enter a number: "))


# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if num % i == 0:
           print(num,"is not a prime number")

           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

"""


"""5"""



"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    print(i)
"""

"""6"""

"""
for i in range(1000,2001):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
"""



