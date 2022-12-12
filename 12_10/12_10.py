# file1 = open('12_10/test_input.txt')
# file1 = open('12_10/test_input_2.txt')
file1 = open('12_10/advent_10_input.txt')

cycles = 0
register = 1
total = 0

screen = [[' ' for _ in range(40)] for _ in range(7)]


for line_no, line in enumerate(file1):
    op, *val = line.strip().split()
    cycles += 1

    if register-1 <= (cycles-1)%40 <= register+1:
        screen[(cycles-1)//40][cycles%40-1] = '#'
    else:screen[(cycles-1)//40][cycles%40-1] = '.'

    if cycles == 20 or (cycles-20)%40==0:
        print(f" cycles {cycles} to get register {register} totaling signal strength { cycles * register}")
        total += (cycles * register)
    if op == "addx":
        cycles += 1
        if cycles == 20 or (cycles-20)%40==0:
            print(f" cycles {cycles} to get register {register} totaling signal strength { cycles * register}")
            total += (cycles * register)
    
        if register-1 <= (cycles-1) % 40 <= register+1:
            screen[(cycles-1)//40][cycles%40-1] = '#'
        else:screen[(cycles-1)//40][cycles%40-1] = '.'

        register += int(val[0])
    print(''.join(screen[cycles//40]))
print(f"total = {total}")

for scline in screen:
    print(''.join(scline))