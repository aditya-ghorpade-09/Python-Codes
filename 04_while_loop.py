f = open("more.txt")

a = f.readline()
while(a != ""):
    print(a)
    a = f.readline()

f.close()