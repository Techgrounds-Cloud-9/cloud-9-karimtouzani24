from re import A


foo = ""

for i in range(1):
    foo += "a"
    for j in range(1):
        foo += "5"
        for k in range(3):
            foo += "|"


print(foo)