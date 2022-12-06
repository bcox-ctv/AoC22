# file1 = open('12_06/test_input.txt')
file1 = open('12_06/advent_6_input.txt')

markerSize = 14
for line in file1:
    for i, _ in enumerate(line):
        if len(set(line[i:i+markerSize:])) == markerSize:
            print(f'found {i+markerSize}')
            break
