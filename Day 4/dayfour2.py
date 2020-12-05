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
        temp_count = 0
        for l in val:
            if l[0] == 'byr':
                if byr(l):
                    temp_count += 1
                else: break
            elif l[0] == 'cid': continue
            elif l[0] == 'iyr':
                if iyr(l):
                    temp_count += 1
                else: break
            elif l[0] == 'eyr':
                if eyr(l):
                    temp_count += 1
                else: break
            elif l[0] == 'hgt':
                if hgt(l):
                    temp_count += 1
                else: break
            elif l[0] == 'hcl':
                if hcl(l):
                    temp_count += 1
                else: break
            elif l[0] == 'ecl':
                if ecl(l):
                    temp_count += 1
                else: break
            elif l[0] == 'pid':
                if pid(l):
                    temp_count += 1
                else: break
            
            if temp_count >= 7:
                count += 1
                break

    return count

def pid(pid):
    if len(pid[1]) != 9: return False
    for num in pid[1]:
        if not num.isdigit(): return False
    return True

def eyr(eyr):
    if len(eyr[1]) == 4 and (int(eyr[1]) >= 2020 and int(eyr[1]) <= 2030):        
        return True
    else: return False

def byr(byr):
    if len(byr[1]) == 4 and (int(byr[1]) >= 1920 and int(byr[1]) <= 2002):
        return True
    else:
        return False

def iyr(iyr):
    if len(iyr[1]) == 4 and (int(iyr[1]) >= 2010 and int(iyr[1]) <= 2020):
        return True
    else:
        return False

def hgt(hgt):
    suffix = hgt[1][-2:]
    if suffix == 'in':
        if int(hgt[1][:-2]) >= 59 and int(hgt[1][:-2]) <= 76: 
            return True
        else:
            return False
    elif suffix == 'cm':
        if int(hgt[1][:-2]) >= 150 and int(hgt[1][:-2]) <= 193:
            return True
        else:
            return False

def hcl(hcl):
    if hcl[1][0] != '#': return False
    hcl_vals = {'0': True, '1': True, '2': True, '3': True, '4': True, '5': True, '6': True, '7': True, '8': True, '9': True, 'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True}
    if len(hcl[1][1:]) != 6: return False
    hcl_count = 0
    for element in hcl[1][1:]:
        if element not in hcl_vals: return False
        else: 
            hcl_count += 1
            continue
    if hcl_count == 6:
        return True
    else:
        return False

def ecl(ecl):
    eye_colors = {'amb': True, 'blu': True, 'brn': True, 'gry': True, 'grn': True, 'hzl': True, 'oth': True}
    if ecl[1] not in eye_colors: return False
    else:
        return True

# Print function for debugging
# def print_valid(k, val):
#     print(k, val)

print(check_valid_values(clean_data()))