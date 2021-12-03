#input = open("input - Kopie.txt", "rt")
input = open("input.txt", "rt")
data = [i.strip() for i in input.readlines()]
#input2 =[int(i) for i in input.readlines()]

def More1():
    data.remove().startswith("0")
    digits = list(zip(*data))
    return digits

def More0():
    data.remove().startswith("1")
    digits = list(zip(*data))
    return digits

digits = list(zip(*data))
ogr, csr = "", ""
print("Part 2:")
print(digits)
print("Startdata: \n",data)

for digit in digits:
    if digit.count("0") > digit.count("1"):
        More0()
    else:
        More1()
    if len(digit) == 1:
        break

print("Restdata: \n",data)

