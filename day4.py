import re


def contains_fields(row):
    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for k, v in row.items():
        if k in valid:
            valid.remove(k)
    if len(valid) == 0:
        return True
    else:
        return False


def test(datas):
    for data in datas:
        if not contains_fields(data):
            return 0

        if int(data['byr']) < 1920 or int(data['byr']) > 2002:
            return 0

        if int(data['iyr']) < 2010 or int(data['iyr']) > 2020:
            return 0

        if len(data['eyr']) != 4 or int(data['eyr']) < 2020 or \
                int(data['eyr']) > 2030:
            return 0

        if data['hgt'].endswith('cm'):
            if 150 <= int(data['hgt']) <= 193:
                pass
            else:
                return 0

        elif data['hgt'].endswith('in'):
            if 59 <= int(data['hgt']) <= 76:
                pass
            else:
                return 0

        else:
            return 0

        if not re.match(r"#[\w]{6}", data['hcl']):
            return 0

        if data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return 0

        
    return 1


input_list = []

f = open('input.txt', 'r')

for line in f:
    input_list.append(line.strip())

counter = 0
data = []

for row in input_list:

    if row == '':
        counter += test(data)
        data = []

    else:
        words = row.split(' ')
        for w in words:
            data.append({w.split(':')[0]: w.split(':')[1]})


print(counter)
