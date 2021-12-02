with open("input.txt", "rt") as text:
    input2 = [i.strip() for i in text.readlines()]

test_data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
down, aim, forward = 0, 0, 0

for data in input2:
    if data.startswith("forward"):
        forward += int(data.split(" ")[1])
        down += (aim*int(data.split(" ")[1]))
    if data.startswith("up"):
        aim -= int(data.split(" ")[1])
    if data.startswith("down"):
        aim += int(data.split(" ")[1])

print("Horizontal position: ", forward, "\nDepth: ", down, "\nSolution: ", forward*down)
