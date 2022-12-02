file1 = open('advent_1_input.txt')
# file1 = open('advent_test.txt')
foods_lines = file1.readlines()
foods = [x.strip() for x in foods_lines]
elf_inventory = []
calories = 0
for food in foods:
    if food == "":
        elf_inventory.append(calories)
        calories = 0
    else:
        calories += int(food.strip())

# max_elf = [(0,0)]
# for elf, inventory in enumerate(elf_inventory):
#     if inventory > max_elf[0][1]:
#         max_elf = [(elf, inventory)] + max_elf
# print(max_elf)
# print(max_elf[0][1]+ max_elf[1][1] + max_elf[2][1])
print(elf_inventory)
elf_inventory.sort(reverse=True)
print(elf_inventory)
print(sum(elf_inventory[:3]))
print(__file__)