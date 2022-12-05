# file1 = open('/home/bcox/advent/12_04/test_input.txt')
file1 = open('/home/bcox/advent/12_04/advent_4_input.txt')
included = 0

for line in file1:
    a, b = line.strip().split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    if ((int(a1) <= int(b1))  & (int(b2) <= int(a2))) or ((int(a1) >= int(b1)) & (int(b2) >= int(a2))):
        included += 1

print(f"included {included}")

overlap = 0
file1.seek(0)
for line in file1:
    a, b = line.strip().split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    if (int(a1) <= int(b1) <= int(a2)) or (int(b1) <= int(a1) <= int(b2)):
        overlap +=1
print(f"overlap {overlap}")