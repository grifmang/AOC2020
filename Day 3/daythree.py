result = []

def findSpot(line, spot):
    while spot > len(line):
        line += line
    return line[spot] == '#'

with open('daythree.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        result.append(line.rstrip('\n'))

count = 0
spot = 3
for line in result[1:]:
    if findSpot(line, spot): count += 1
    spot += 3

print(count)