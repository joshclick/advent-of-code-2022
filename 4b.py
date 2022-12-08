lines = []
with open('4-input.txt') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]
# print(lines)


contains = 0
for line in lines:
	a, b = line.split(',')
	a_start, a_end = a.split('-')
	b_start, b_end = b.split('-')
	a1, a2, b1, b2 = int(a_start), int(a_end), int(b_start), int(b_end)
	# if a_start == b_start and b_end == a_end:
	# 	continue
	a = set([i for i in range(a1, a2+1)])
	b = set([i for i in range(b1, b2+1)])
	if len(a.intersection(b)):
		contains += 1


print(contains)

