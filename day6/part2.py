my_file = open("./data.txt", "r")
data=my_file.read()
dico= set()
cursor=0
while len(dico)<14:
    items=data[cursor:cursor+14]
    dico.clear()
    for item in items:
        dico.add(item)
    print(dico)
    cursor+=1

my_file.close()
print(cursor+13)
#+13 because +14-1