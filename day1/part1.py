f = open('./data.txt', "r")

#first part
max_calories = 0
actual_elf_calories = 0

for line in f:
    
    if line == '\n':
        if actual_elf_calories>max_calories:
            max_calories=actual_elf_calories
        actual_elf_calories = 0

    else:
        actual_elf_calories=int(line) + actual_elf_calories
        



print(max_calories)
f.close