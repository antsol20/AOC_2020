input = []

f = open('input.txt', 'r')

for line in f:
    input.append(line.strip())

total_answers = []
answers = []

for line in input:

    if line == "":
        total_answers.append(set(answers))
        answers = []

    else:
        for chr in line:
            answers.append(chr)

print(len(total_answers[0]))
print(len(total_answers[1]))
counter = 0
for res in total_answers:
    counter += len(res)

print(counter)
