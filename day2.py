from utils.input import read_input_from_site
from collections import defaultdict

input_list = read_input_from_site(2)

# 5-6 s: zssmssbsms
part1 = 0

for line in input_list:
    words = line.split(' ')
    ch_map = defaultdict(int)
    for chr in words[2]:
        ch_map[chr] = ch_map[chr] + 1
    min = int(words[0].split('-')[0])
    max = int(words[0].split('-')[1])
    act = ch_map[words[1][0]]
    print(min, max, act)
    if (act <= max and act >= min):
        part1 += 1

print(part1)

part2 = 0
# 5-6 s: zssmssbsms
for line in input_list:
    words = line.split(' ')
    pos1 = int(words[0].split('-')[0]) - 1
    pos2 = int(words[0].split('-')[1]) - 1
    charpos1 = words[2][pos1]
    charpos2 = words[2][pos2]
    letter = words[1][0]

    if charpos1 == letter:
        if charpos2 != letter:
            part2 += 1

    if charpos2 == letter:
        if charpos1 != letter:
            part2 += 1


print(part2)
