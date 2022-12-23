my_file = open("./data.txt", "r")
data=my_file.read()
dico= set()
cursor=0
while len(dico)<4:
    items=data[cursor:cursor+4]
    dico.clear()
    for item in items:
        dico.add(item)
    print(dico)
    cursor+=1

my_file.close()
print(cursor+3)
#+3 because +4-1