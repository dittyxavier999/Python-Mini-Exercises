
# patternn 
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)


for i in range(10, 0, -1):
    for j in range(i):
        print("*", end="")
    print()