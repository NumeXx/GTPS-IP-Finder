# Code By NumeX
# Kang Col1 (KIPAS)

text = input("Enter Host : ")
ok = open(text, "r").readlines()

for i in ok:
    if i[0].startswith("#"):
        pass
    elif not i[0].isdigit():
        pass
    else:
        print(str(i)) 
