result = []

with open('dayone.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        result.append(int(line))

sums = []

for index, num in enumerate(result):
    for ind, nums in enumerate(result[index+1:]):
            if num + nums == 2020:
                print(nums*num)