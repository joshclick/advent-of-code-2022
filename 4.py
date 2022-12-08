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
	if (
		(a1 <= b1 and a2 >= b2) or
		(b1 <= a1 and b2 >= a2)
		):
		contains += 1

print(contains)

