age = int(input("Enter the age - "))

if(age>=18):
    print("You are an Adult")
elif(age<0):
    print("You entered negative invalid age")
elif(age==0):
    print("You entered zero invalid age")
else:
    print("You are not an Adult")

print("End!")