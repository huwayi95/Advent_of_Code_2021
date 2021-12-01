input = open("input.txt", "rt")
#input2 = [i.strip() for i in input.readlines()]
input2 =[int(i) for i in input.readlines()]
test_depths = [199,200,208,210,200,207,240,269,260,263]

input3 =[]
input2tmp = 0
for int in input2[:-2]:
    if input2[input2tmp+2] != '':
        input3.append(input2[input2tmp]+input2[input2tmp+1]+input2[input2tmp+2])
        input2tmp+=1

tmp=0
count=0
for line in input3:
    if tmp == 0:
        tmp = line
        continue
    if line > tmp:
        tmp = line
        count+=1
    elif line < tmp:
        tmp = line

print(count)

