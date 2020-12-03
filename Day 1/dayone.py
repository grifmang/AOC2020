result = []

with open('puzzle_one_inputs.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        result.append(int(line))

sums = []

for index, num in enumerate(result):
    for ind, nums in enumerate(result[index+1:]):
        for i, n in enumerate(result[ind+1:]):
            if num + nums + n == 2020:
                print(nums*num*n)