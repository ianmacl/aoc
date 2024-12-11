import json

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

dirs = {
    '.': []
}

def add_dir(current_path, name):
    location = "/".join(current_path) + '/' + name
    if location in dirs:
        print("Dir already exists - could be error")
    else:
        dirs[location] = []

def add_file(current_path, name, size):
    location = "/".join(current_path)
    
    if not location in dirs:
        print("Unseen dir - probably an error")
    dirs[location].append({
        'file': name,
        'size': size
    })


def get_size(files):
    return sum([file['size'] for file in files])

files = 0
current_path = ['.']
for line in lines:
    if line.startswith('$ cd '):
        line = line.removeprefix('$ cd ')
        if line == '/':
            current_path = ['.']
        elif line == '..':
            current_path.pop()
        else:
            current_path.append(line.strip())
    elif line.startswith('$ ls'):
        pass
    elif line.startswith('dir '):
        add_dir(current_path, line.removeprefix('dir '))
    else:
        (size, name) = line.split()
        add_file(current_path, name, int(size))
        files += 1

#print(dirs)
dir_sizes = {}
for dir in dirs:
    dir_size = sum([get_size(dirs[sizedir]) for sizedir in dirs if sizedir.startswith(dir + '/')]) + get_size(dirs[dir])
    print(dir + ' ' + str(dirs[dir]))
    print('%s - %d' % (dir, dir_size))
    dir_sizes[dir] = dir_size

#print(dir_sizes)
print(files)

print(json.dumps(dirs, indent=2))
for dir in dir_sizes:
    print('%s - %d' % (dir, dir_sizes[dir]))
print(sum([dir_sizes[dir] for dir in dir_sizes if dir_sizes[dir] <= 100000]))

space_available = 70000000 - dir_sizes['.']
space_required = 30000000
space_to_delete = space_required - space_available

print(sorted([dir_sizes[dir] for dir in dir_sizes if dir_sizes[dir] >= space_to_delete]))
print(sorted([dir_sizes[dir] for dir in dir_sizes if dir_sizes[dir] >= space_to_delete])[0])