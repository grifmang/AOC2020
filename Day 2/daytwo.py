result = []

with open('daytwo.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        result.append(line)

count = 0

for val in result:
    val = val.split(':')
    string = ''.join(list(map(str, val[1]))).rstrip('\n').lstrip(' ')
    letter = val[0].split(' ')[1]
    nums = list(map(int, val[0].split(' ')[0].split('-')))
    if string.count(letter) >= nums[0] and string.count(letter) <= nums[1]: count += 1

print(count)