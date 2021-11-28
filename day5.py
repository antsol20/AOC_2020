input = []

f = open('input.txt', 'r')

for line in f:
    input.append(line.strip())


maxlist = []

for row in input:
    rownum = 0
    colnum = 0
    for i in range(7):
        if row[i] == 'B':
            rownum += 2 ** (6 - i)
    
    for i in range(0, 3):
        if row[i+7] == 'R':
            colnum += 2 ** (2 - i)
    
    seat_id = (rownum * 8) + colnum
    maxlist.append(seat_id)

print(max(maxlist))

maxlist.sort()
for idx, item in enumerate(maxlist):
    if maxlist[idx + 1] != item + 1:
        print(item, item + 1)




