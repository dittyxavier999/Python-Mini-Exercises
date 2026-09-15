#Create a variable txt with the value "Hello, World!"

txt = "Hello World!"

for i in range(len(txt) + 1):
    print(txt[:i])


txt1 = '''Thank you Jesus'''

print(txt)

for i in range(17):
    if i < 16:
        print(txt1[:i])
    else:
        print(txt1)


        txt3 = "Pray for us mumma mary!"

for i in range(len(txt3) + 1):
    print(txt3[:i])


for k in range(9):
    print(k)

# 3 Print txt converted to upper case


# 4 Create a variable name with the value "Python"

w = "python"
print(w[::-2])
print (w[::2])
print (w[:])
print(w[::-1])

mal = "Malayalam"
for i in range  (len(mal)):
 print (mal[i])


# reverse print Malayalam line by line
mal = "Malayalam"
print()


for i in range(len(mal) - 1, -1, -1):
    print(mal[i])

    mal = "Malayalam"

for i in range(len(mal)):
    print(mal[i])
    print()
    # 5 Use an f-string to print "I love Python" using the name variable