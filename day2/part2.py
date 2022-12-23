f = open('./data.txt', "r")

result = 0
for line in f:

    if line[0].split() == ['A']: #rock
        if line[2].split() == ['X']:#loss (Scissors)
            result +=3
        if line[2].split() == ['Y']:#draw (rock)
            result +=4
        if line[2].split() == ['Z']:#win (paper)
            result +=8
    
    if line[0].split() == ['B']:#paper 
        if line[2].split() == ['X']:#loss (rock)
            result +=1
        if line[2].split() == ['Y']:#draw (paper)
            result +=5
        if line[2].split() == ['Z']:#win (Scissors)
            result +=9

    if line[0].split() == ['C']:#Scissors 
        if line[2].split() == ['X']:#loss (paper)
            result +=2
        if line[2].split() == ['Y']:#draw (Scissors)
            result +=6
        if line[2].split() == ['Z']:#win (rock)
            result +=7
print (result)