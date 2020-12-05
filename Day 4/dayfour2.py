def clean_data():
    valid_passports = {}
    counter = 1
    with open('dayfour.txt', 'r') as file:
        lines = file.read().split('\n\n')
        for line in lines:
            temp = []
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
                            temp.append(x)
                else:
                    if l.split(':')[0] in check_tags:
                        check_tags[l.split(':')[0]] += 1
                        temp.append(l.split(':'))

            valid = True
            val_count = 0
            for k, v in check_tags.items():
                if v == 0 and k != 'cid': valid = False
                elif v == 1: val_count += 1

            if val_count >= 7 and valid: 
                valid_passports[counter] = temp
                counter += 1


    return valid_passports

def check_valid_values(passports):
    count = 0
    for val in passports.values():
        valid = False
        for l in val:
            if l[0] == 'byr':
                if len(l[1]) != 4: break
                if (int(l[1]) < 1920 or int(l[1]) > 2002):
                    break
                print_valid(l[0], l[1])
            elif l[0] == 'cid': continue
            elif l[0] == 'iyr':
                if len(l[1]) != 4: break
                if (int(l[1]) < 2010 or int(l[1]) > 2020):
                    break
                print_valid(l[0], l[1])
            elif l[0] == 'eyr':
                if len(l[1]) != 4: break
                if (int(l[1]) < 2020 or int(l[1]) > 2030):
                    break
                print_valid(l[0], l[1])
            elif l[0] == 'hgt':
                suffix = l[1][-2:]
                if suffix != 'in' or suffix != 'cm': break
                if suffix == 'in' and (int(l[1][:-2]) < 59 or int(l[1][:-2]) > 76): break
                if suffix == 'cm' and (int(l[1][:-2]) < 150 or int(l[1][:-2]) > 193): break
                print_valid(l[0], l[1])
            elif l[0] == 'hcl':
                if l[1][0] != '#': break
                hcl_vals = {'0': True, '1': True, '2': True, '3': True, '4': True, '5': True, '6': True, '7': True, '8': True, '9': True, 'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True}
                if len(l[1][1:]) != 6: break
                for element in l[1][1:]:
                    if element not in hcl_vals: break
                print_valid(l[0], l[1])
            elif l[0] == 'ecl':
                eye_colors = {'amb': True, 'blu': True, 'brn': True, 'gry': True, 'grn': True, 'hzl': True, 'oth': True}
                if l[1] not in eye_colors: break
                print_valid(l[0], l[1])
            elif l[0] == 'pid':
                if len(l[1]) != 9: break
                for num in l[1]:
                    if not num.isdigit(): break
                print_valid(l[0], l[1])
            valid = True
        if valid: count += 1

    return count

def print_valid(k, val):
    print(k, val)


print(check_valid_values(clean_data()))