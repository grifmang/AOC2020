def highest_seat():
    high_seat = 0
    with open('dayfive.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip('\n')
            row = row_search(line[:7])
            col = col_search(line[7:])
            high_seat = max(high_seat, (row * 8) + col)
    return high_seat

def row_search(string):
    row_range = [x for x in range(127)]
    for num in range(len(string) - 1):
        if string[num] == 'F': row_range = row_range[:len(row_range) // 2]
        else: row_range = row_range[len(row_range) // 2 + 1:]
    return row_range[0]


def col_search(string):
    col_range = [x for x in range(8)]
    for num in range(len(string) - 1):
        if string[num] == 'R': col_range = col_range[len(col_range) // 2:]
        else: col_range = col_range[:len(col_range) // 2 + 1]
    return col_range[1] if string[-1] == 'R' else col_range[0]

print(highest_seat())