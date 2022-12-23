f = open('./data.txt', "r")

result = 0
for line in f:

    if line[2].split() == ['X']: #rock +1
        if line[0].split() == ['A']:#Rock
            result +=4
        if line[0].split() == ['B']:#Paper
            result +=1
        if line[0].split() == ['C']:#Scissors
            result +=7
    
    if line[2].split() == ['Y']:#paper +2
        if line[0].split() == ['A']:#Rock
            result +=8
        if line[0].split() == ['B']:#Paper
            result +=5
        if line[0].split() == ['C']:#Scissors
            result +=2

    if line[2].split() == ['Z']:#Scissors +3
        if line[0].split() == ['A']:#Rock
            result +=3
        if line[0].split() == ['B']:#Paper
            result +=9
        if line[0].split() == ['C']:#Scissors
            result +=6
print (result)