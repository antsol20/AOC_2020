from utils.input import read_input_from_site

input_list = read_input_from_site(1)

for x in input_list:
    for y in input_list:
        for z in input_list:
            if int(x) + int(y) + int(z) == 2020:
                ans = int(x) * int(y) * int(z)
                print(ans)
