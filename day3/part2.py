f = open('./data.txt', "r")

result = 0
lettres=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
three_lines= []

for line in f:
    three_lines.append(line)

    if len(three_lines)%3 == 0:
        
        for lettre in three_lines[0]:
            if lettre in three_lines[1] and lettre in three_lines[2]:

                index = lettres.index(lettre)+1
                result+=index
                three_lines= []
                break


        

print(result)