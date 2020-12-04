def part1(passports):
    valid = 0
    for a in passports:
        d = {}
        index = 0
        for b in a:
            b = b.split(':')
            d[b[index]] = b[index + 1]
        if(len(d) <= 7):
            try:
                d['cid']    
            except Exception as e:
                if(len(d) == 7):
                    valid += 1
        else:
            valid += 1
    return valid

def part2(passports):
    valid = 0
    byr = iyr = eyr = hgt = hcl = ecl = pid = cid = ''
    a_ecl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    for a in passports:
        d = {}
        index = 0
        for b in a:
            b = b.split(':')
            d[b[index]] = b[index + 1]
        try:
            byr = d['byr']
        except Exception as e:
            continue
        try:
            iyr = d['iyr']
        except Exception as e:
            continue
        try:
            eyr = d['eyr']
        except Exception as e:
            continue
        try:
            hgt = d['hgt']
        except Exception as e:
            continue
        try:
            hcl = d['hcl']
        except Exception as e:
            continue
        try:
            ecl = d['ecl']
        except Exception as e:
            continue
        try:
            pid = d['pid']
        except Exception as e:
            continue
        try:
            d['cid']
        except Exception as e:
            pass
        
        if not (int(byr) >= 1920 and int(byr) <= 2002):
            continue
        if not (int(iyr) >= 2010 and int(iyr) <= 2020):
            continue
        if not (int(eyr) >= 2020 and int(eyr) <= 2030):
            continue
        if hgt[len(hgt) - 2:] == 'cm':
            h = int(hgt[:len(hgt) - 2])
            if not (h >= 150 and h <= 193):
                continue
        elif hgt[len(hgt) - 2:] == 'in':
            h = int(hgt[:len(hgt) - 2])
            if not (h >= 59 and h <= 76):
                continue
        else:
            continue
        if len(hcl) != 7:
            continue
        if ecl not in a_ecl:
            continue
        if len(pid) != 9:
            continue
        valid += 1
    return valid

with open('input.txt') as f:
   lines = f.readlines()

full = []
part = []
cnt = 0
for c, line in enumerate(lines):
    line = line.rstrip('\n')
    if line == '' or c == len(lines) - 1:
        if c == len(lines) - 1:
            part.append(line)
        full.append(part)
        part = []
    else:
        part.append(line)
afull = []
for line in full:
    new = []
    for x in line:
        new.extend(x.split(' '))
    afull.append(new)

print(part1(afull))
print(part2(afull))
