count = 0

with open('dayfour.txt', 'r') as file:
    lines = file.read().split('\n\n')
    for line in lines:
        check_tags = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0, 'cid': 0}
        line = line.split(' ')
        for l in line:
            if l.count(':') > 1:
                l = l.split('\n')
                # check line[l] with a line break in them
                for x in l:
                    x = x.split(':')
                    if x[0] in check_tags:
                        check_tags[x[0]] += 1
            else:
                if l.split(':')[0] in check_tags:
                    check_tags[l.split(':')[0]] += 1

        valid = True
        val_count = 0
        for k, v in check_tags.items():
            if v == 0 and k != 'cid': valid = False
            elif v == 1: val_count += 1

        if val_count >= 7 and valid: count += 1

print(count)