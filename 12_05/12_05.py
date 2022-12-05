# file1 = open('12_05/test_input.txt')
file1 = open('12_05/advent_5_input.txt')

tmp = file1.readlines()
half = 0
cargo = []
directions = []
stacks = {}
for line in tmp:
    if line.strip() == "":
        half = 1
    elif half == 0:
        cargo.append(line)
    else:
        directions.append(line)

# print(cargo)
for row in cargo:
    row = row.replace('\n', '')
    crates = [row[i:i+3] for i in range(0, len(row), 4)]
    for stack in range(len(crates)):
        if '[' in crates[stack]:
            stacks.setdefault(stack +1, []).append(crates[stack].replace('[', '').replace(']', ''))

for move in directions:
    num_crates, source, target = [int(i) for i in move.split() if i.isdigit()]
    stacks[target][:0] = stacks[source][:num_crates:][::-1]
    stacks[source] = stacks[source][num_crates:]

print("".join([stacks[stack+1][0] for stack in range(len(stacks))]))

stacks = {}
for row in cargo:
    row = row.replace('\n', '')
    crates = [row[i:i+3] for i in range(0, len(row), 4)]
    for stack in range(len(crates)):
        if '[' in crates[stack]:
            stacks.setdefault(stack +1, []).append(crates[stack].replace('[', '').replace(']', ''))

for move in directions:
    num_crates, source, target = [int(i) for i in move.split() if i.isdigit()]
    stacks[target][:0] = stacks[source][:num_crates:][::1]
    stacks[source] = stacks[source][num_crates:]

print("".join([stacks[stack+1][0] for stack in range(len(stacks))]))