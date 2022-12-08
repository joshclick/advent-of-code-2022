lines = []
with open('7-input') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]

class Folder:
	name = ''
	children = None
	parent = None

	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.children = {}

	def __repr__(self):
		return self.name


class File:
	size = 0
	name = ''

	def __init__(self, size, name):
		self.name = name
		self.size = size

	def __repr__(self):
		return self.name


base = Folder('base', None)
root = Folder('/', base)
base.children['/'] = root

i = 0
curr_dir = base
while i < len(lines):
	line = lines[i]
	if line[0] == '$':
		cmd = line[2:4]
		if cmd == 'cd':
			new_dir = line[5:]
			if new_dir == '..':
				if curr_dir.parent:
					curr_dir = curr_dir.parent
				else:
					print('already at root, not going further')
			else:
				if new_dir not in curr_dir.children.keys():
					curr_dir.children[new_dir] = Folder(new_dir, parent=curr_dir)
				curr_dir = curr_dir.children[new_dir]
			i += 1
		elif cmd == 'ls':
			i += 1
			line = lines[i]
			while line[0] != '$':
				a, b = line.split()
				if b not in curr_dir.children.keys():
					if a == 'dir':
						new_item = Folder(b, parent=curr_dir)
					else:
						new_item = File(int(a), b)
					curr_dir.children[b] = new_item
				i += 1
				if i >= len(lines):
					break
				line = lines[i]

		else:
			print('unknown cmd!')
			break
	else:
		print(line)

print('done parsing cmds')

# 100000
dir_sizes = []
def dfs(node):
	global dir_sizes
	curr_size = 0
	for key, child in node.children.items():
		if isinstance(child, Folder):
			curr_size += dfs(child)
		else:
			curr_size += child.size
	dir_sizes.append(curr_size)
	return curr_size


dfs(root)
at_most_100000_total = 0
for d in dir_sizes:
	if d <= 100000:
		at_most_100000_total += d
print(at_most_100000_total)
# 2142238 too high
# 1723892


# 7b

# 100000
dir_sizes = {}
def dfs(node):
	global dir_sizes
	curr_size = 0
	for key, child in node.children.items():
		if isinstance(child, Folder):
			curr_size += dfs(child)
		else:
			curr_size += child.size
	dir_sizes[node.name] = curr_size
	return curr_size


dfs(root)


min_dir = 70000000
for size in dir_sizes:
	if size >= 6552309 and size < min_dir:
		min_dir = min(min_dir, size)

print(min_dir)

# total root size - 46552309
# 70000000 - 46552309 = 23447691 unused
# 30000000 - 23447691 = 6552309 needed to free up
# need to find smallest dir larger than 6552309


