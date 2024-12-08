from itertools import starmap

input = open("input.txt")
left_list = []
right_list = []
for line in input:
    left, right = line.split()
    l, r = int(left), int(right)
    left_list.append(l)
    right_list.append(r)

left_list.sort()
right_list.sort()

print(sum(starmap(lambda l, r: abs(l - r), zip(left_list, right_list))))

# Part Two

similarity_index = {}
for r in right_list:
    if r in similarity_index:
        similarity_index[r] += 1
    else:
        similarity_index[r] = 1

print(sum(map(lambda l: l * similarity_index.get(l, 0), left_list)))
