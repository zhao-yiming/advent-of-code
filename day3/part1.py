f = open('./data.txt', "r")

result = 0
lettres=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
for line in f:

    size = len(line)
    middle= int((size-1)/2)

    first_rucksack= line[0:middle]
    second_rucksack= line[middle:-1]
    
    for lettre in first_rucksack:
        if lettre in second_rucksack:
            index = lettres.index(lettre)+1
            result+=index
            break
    
print(result)