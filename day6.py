import string
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

counter = 0
for res in total_answers:
    counter += len(res)

print("Part 1:")
print(counter)

# ########################part 2#############
all_yes = set(string.ascii_lowercase)
counter = 0
for line in input:
    if line == "":
        counter += len(all_yes)
        all_yes = set(string.ascii_lowercase)

    else:
        for letter in set(string.ascii_lowercase):
            if letter not in line and letter in all_yes:
                all_yes.remove(letter)

print("Part 2:")
print(counter)
