input = open("input - Kopie.txt", "rt")
#input = open("input.txt", "rt")
data = [i.strip() for i in input.readlines()]
#input2 =[int(i) for i in input.readlines()]

digits = list(zip(*data))
gamma, epsilon = "", ""

for digit in digits:
    if digit.count("0") > digit.count("1"):
        gamma+= "0"
        epsilon+= "1"
    else:
        gamma+= "1"
        epsilon+="0"
print("Part 1:")
print("Gamma:   ",int(gamma, 2))
print("Epsilon: ",int(epsilon, 2))
print("Both:    ",int(gamma, 2)*int(epsilon, 2))
