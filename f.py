
# python easy to  learn , versatile , language and active community, portable, high level languae
#  python variables. data type int, complex num, floating numbers, string , 
# capitalize(), casefold(), eg:  x= txt.casefold() # small letter il print chyum,
print("hello world")
a=2
b=3
c= a+b
print(c)

name = "python"
for i in range(0, 10, 2):
  print(f"Ditty likes of {name}") 
# list is a collection of data items they enclosed in square brackets and speprated by index for example 
# set of funcion
l =["apple", "banana", "cherry", "apple"]

#list → []
#tuple → ()
#set → {}
#dictionary → {'key': 'value'}

 # fruits.remove("banana") 
 #print (fruits)
 # other functions append(), remove(), list is mutable but tuple immutable no change allowed in tuple use normal () brankets
 # set is a unique collection of data , no duplicates saved in set x = set(1,2,1,2,3)  set is unorderded unique elements
 # print (x)
#se = set(1,2,1,2,3)
#print (se)

vet = set(['apple', 'banana', 'cherry', 'apple'])

print(vet)
# unique elements only list when use set(l)


s=set(l)

print(s)
print (len(s))
print (len(l))


# dictionairs

car = {"brand": "Ford", "model": "mustang", "year": 1994}
x = car.items()  # ella item tuples created akkum out put il
print(x)

# arithametic operations
# addition
print("-------1. Arithmetic operators----")
a = 10
b = 3

# Addition (+)
print(f"Addition(a+b):{a+b}")

# subtraction (-)
print(f"Subtraction(a-b):{a-b}")

# Multiplication(*)
print(f"Multiplication(a*b):{a*b}")

# Division
print(f"Division (a/b):{a/b}")

#2 program

age = 20
has_id = False

# check if the person is enough ( >=18 ) AND has an ID.

can_enter = (age >= 18) and has_id== True

if can_enter == True :
  print("combined logic : Access Granded")
else:
  print("combined logic : Access Denied")
