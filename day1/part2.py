#second part
f = open('./data.txt', "r")


elf_calories = 0
calories_lsit=[]

for line in f:
    
    if line == '\n':
        calories_lsit.append(elf_calories)
        elf_calories = 0

    else:
        elf_calories+=int(line)
f.close

print(sorted(calories_lsit, reverse=True)[:3])
