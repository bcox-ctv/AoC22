# file1 = open('12_09/test_input.txt')
# file1 = open('12_09/test_input_2.txt')
file1 = open('12_09/advent_9_input.txt')

def is_not_touching(hx, hy, tx, ty):
    if abs(hy-ty)+abs(hx-tx)>=3 : # dif row and col
        if hy<ty : ty -=1 
        else: ty +=1
        if hx<tx : tx -=1 
        else: tx +=1
    elif hx==tx and abs(hy-ty)>=2:
        #same col, dif row
        if hy<ty : ty -=1 
        else: ty +=1
    elif hy==ty and abs(hx-tx)>=2:
        #same row dif col
        if hx<tx : tx -=1 
        else: tx +=1
    return (tx,ty)

tail_record = {(0,0)}
# rope=[[0,0],[0,0]]
rope=[[0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0]]

for line in file1:
    direction, count = line.strip().split()
    count = int(count)

    for i in range(count):
        if direction == "R":
            rope[0][0] +=1
        elif direction == "L":
            rope[0][0] -=1
        elif direction == "U":
            rope[0][1] += 1
        else: # direction == "D"
            rope[0][1] -= 1

        # tx, ty = is_not_touching(hx, hy, tx, ty)
        # tail_record.add((tx,ty))
        for knot in range(1, len(rope)):
            hx = rope[knot-1][0]
            hy = rope[knot-1][1]
            tx = rope[knot][0]
            ty = rope[knot][1]
            rope[knot] = is_not_touching(hx, hy, tx, ty)
            if knot == len(rope)-1:
                tail_record.add((rope[knot][0], rope[knot][1]))

print(len(tail_record))