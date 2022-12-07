import dpath
import json

global supertotal
supertotal = 0
global delete_size
delete_size = 0
needed_size = 6876531

def dirsize(folder):
    global supertotal
    global delete_size
    total = 0
    for key, value in folder.items():
        if type(value) is dict:
            child_size = dirsize(value)
            print(f"directory {key} of size {child_size}")
            if child_size <= 100000: supertotal += child_size
            if child_size > needed_size and (child_size < delete_size or delete_size==0):
                delete_size = child_size
            total += child_size
        else:
            total += int(value)
            
    return total    

# file1 = open('12_07/test_input.txt')
file1 = open('12_07/advent_7_input.txt')

direct = {}
full_path = ""
pwd = ""
ls = False
for line in file1:
    cmd, *rest = line.split()
    if cmd == "$":
        if rest[0] == 'cd':
            if rest[1] == "/":
                full_path = ""
            elif rest[1] == "..":
                pwd = full_path[:-1]
                full_path = "/".join(full_path.split("/")[:-1])
            else:
                pwd = rest[1]
                full_path +=  f"/{pwd}"
    elif cmd.isdigit():
        dpath.new(direct,f"{full_path}/[{rest[0]}]",cmd)       
    

print(json.dumps(direct, indent=4, sort_keys=True))
print(dirsize(direct))
print(supertotal)
print(70000000-supertotal)
print(delete_size)