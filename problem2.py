def convert(f):
    return (5/9)*(f-32)

f = int(input("Enter Degree in Farenheit - "))
r = convert(f)
a = round(r,2)

print(f"{a} Degree Celcius")