lines = []
with open('6-input') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]

line = lines[0]
for i in range(0, len(line)):
	x = set([c for c in line[i:i+4]])
	if len(x) == 4:
		print(i+4)
		break



# WHTLRMZRC
