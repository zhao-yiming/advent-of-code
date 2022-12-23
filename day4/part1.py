f = open('./data.txt', "r")

result = 0
for line in f:
    NoDot=line.replace(',','-')
    NoNew_line=NoDot.replace('\n','')
    Number_liste =NoNew_line.split('-')

    if (int(Number_liste[0])<= int(Number_liste[2]) and int(Number_liste[1])>=int(Number_liste[3])) or( int(Number_liste[0])>= int(Number_liste[2]) and int(Number_liste[1])<=int(Number_liste[3])):
        result+=1
print(result)