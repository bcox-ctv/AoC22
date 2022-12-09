# file1 = open('12_08/test_input.txt')
file1 = open('12_08/advent_8_input.txt')

forest = []
for line in file1:
    int_list = [int(x) for x in list(line.strip())]
    forest.append(int_list)

def test_tree(i, j, forest):
    
    visible_w = all(tree < forest[i][j] for tree in forest[i][:j])
    visible_e = all(tree < forest[i][j] for tree in forest[i][::-1][: len(forest[i]) - j - 1])

    forest_col = [row[j] for row in forest]
    visible_n = all(tree < forest[i][j] for tree in forest_col[:i])
    visible_s = all(tree < forest[i][j] for tree in forest_col[::-1][: len(forest_col) - i - 1])

    return visible_w or visible_e or visible_n or visible_s

def visibility(i, j, forest):
    forest_col = [row[j] for row in forest]
    view_up = 0
    for tree in forest_col[:i][::-1]:
        view_up += 1
        if tree >= forest[i][j]:
            break

    view_left = 0
    for tree in forest[i][:j][::-1]:
        view_left += 1
        if tree >= forest[i][j]:
            break

    view_down = 0
    for tree in forest_col[i+1:]:
        view_down += 1
        if tree >= forest[i][j]:
            break

    view_right  = 0
    for tree in forest[i][j+1:]:
        view_right += 1
        if tree >= forest[i][j]:
            break
    return view_down * view_right * view_up * view_left

counter = 0
max_score = 0
for i in range(len(forest)):
    for j in range(len(forest[i])):
        if test_tree(i, j, forest): counter += 1
        vis_score = visibility(i,j,forest)
        if vis_score > max_score: max_score = vis_score

print(f"{counter} visible trees")
print(f"{max_score} max scenic score")
