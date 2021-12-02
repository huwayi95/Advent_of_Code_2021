input = open("input.txt", "rt")
input2 = [i.strip() for i in input.readlines()]
#input2 =[int(i) for i in input.readlines()]
test_data = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

down=0
aim=0

forward2 = 0
depth = 0
for data in input2:
    if data.startswith("forward"):
        forward2+=int(data.split(" ")[1])
        down+=(aim*int(data.split(" ")[1]))
    if data.startswith("up"):
        aim -= int(data.split(" ")[1])
    if data.startswith("down"):
        aim += int(data.split(" ")[1])

print("Horizontal position: ", forward2,"\nDepth: ", down,"\nSolution: ", forward2*down)







