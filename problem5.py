def pat(n):
    if(n==0):
        return
    else:
        print("*"*n)
        pat(n-1)

n = int(input("Enter Number - "))

pat(n)