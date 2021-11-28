import math

input_list = []

f = open('input.txt', 'r')

for line in f:
    input_list.append((line.strip())*1000)


routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answers = []


for (dc, dr) in routes:
    r = 0
    c = 0
    score = 0
    while r+1 < len(input_list):
        c += dc
        r += dr
        if input_list[r][c] == '#':
            score += 1

    answers.append(score)


print(answers)
print(math.prod(answers))

