lines = []
with open('5-input') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]

stacks = [[] for i in range(9)]
for line in lines:
	items = line.split(' ')
	for i in range(len(items)):
		c = items[i][1]
		if c == '!':
			continue
		else:
			stacks[i].insert(0, c)

lines2 = []
with open('5a-input') as f:
    lines2 = f.readlines()
lines2 = [l[:-1] for l in lines2]

print(lines2)
for line in lines2:
	words = line.split(' ')
	count, a, b = int(words[1]), int(words[3]), int(words[5])
	temp = stacks[a-1][-count:]
	stacks[a-1] = stacks[a-1][:-count]
	stacks[b-1] += temp


print(''.join([s[-1] for s in stacks]))


# WHTLRMZRC
