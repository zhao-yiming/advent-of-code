f = open('./data.txt', "r")

result = 0
for line in f:
    NoDot=line.replace(',','-')
    NoNew_line=NoDot.replace('\n','')
    Number_liste =NoNew_line.split('-')

    if int(Number_liste[0]) in range(int(Number_liste[2]),int(Number_liste[3])+1) or int(Number_liste[1]) in range(int(Number_liste[2]),int(Number_liste[3])+1):
        result+=1

    elif int(Number_liste[2]) in range(int(Number_liste[0]),int(Number_liste[1])+1) or int(Number_liste[3]) in range(int(Number_liste[0]),int(Number_liste[1])+1):
        result+=1
print(result)