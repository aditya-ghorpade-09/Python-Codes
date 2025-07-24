def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

x = int(input("Enter Number - "))
y = int(input("Enter Number - "))
z = int(input("Enter Number - "))

r = greatest(x,y,z)

print("Greatest number is -",r)