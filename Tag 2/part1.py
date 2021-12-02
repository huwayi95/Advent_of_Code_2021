input = open("input.txt", "rt")
input2 = [i.strip() for i in input.readlines()]
#input2 =[int(i) for i in input.readlines()]
test_data = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

forward = []
up = []
down = []
aim = 0
down_ges = 0
up_ges= 0
forward_ges = 0

for data in input2:
    if "forward" in data:
        tmp = data.split(" ")
        forward.append(tmp[1])
for data in forward:
    forward_ges+=int(data)

for data in input2:
    if "up" in data:
        tmp = data.split(" ")
        up.append(tmp[1])
for data in up:
    up_ges+=int(data)

for data in input2:
    if "down" in data:
        tmp = data.split(" ")
        down.append(tmp[1])
for data in down:
    down_ges+=int(data)

print("Forward: ",forward_ges, "\nDown: ", down_ges, "\nUp: ", up_ges, "\nDepth: ", down_ges - up_ges)
depth_ges = down_ges-up_ges
print("Lösung: ",forward_ges*depth_ges)
