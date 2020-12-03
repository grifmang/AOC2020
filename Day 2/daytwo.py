result = []

with open('daytwo.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        result.append(line)
print(len(result))
return_result = []
count = 0

for val in result:
    val = val.split(':')
    string = ''.join(list(map(str, val[1]))).rstrip('\n').lstrip(' ')
    letter = val[0].split(' ')[1]
    nums = list(map(int, val[0].split(' ')[0].split('-')))
    matches = [string[nums[0]-1], string[nums[1]-1]]
    if matches.count(letter) == len(matches): continue
    if letter in matches: return_result.append([letter, matches, count, string])
    count += 1

# [print(x) for x in return_result]
print(len(return_result))