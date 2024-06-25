str = input()
l = ""

for i in str:
    if i.isupper() == True:
        l += i.lower()
    elif i.islower() == True:
        l += i.upper()
print(l)