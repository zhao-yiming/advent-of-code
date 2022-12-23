puzzle=[['t','f','v','z','c','w','s','q'],['b','r','q'],['s','m','p','q','t','z','b'],
        ['h','q','r','f','v','d'],['p','t','s','b','d','l','g','j'],['z','t','r','w'],
        ['j','r','f','s','n','m','q','h'],['w','h','f','n','r'],['b','r','p','q','t','z','j']]
f = open('./data.txt', "r")

for line in f:
    number,departure,arrivate=[int(s) for s in line.split() if s.isdigit()]
    select_items=puzzle[departure-1][0:number]
    for item in select_items:
        puzzle[arrivate-1].insert(0,item)
        puzzle[departure-1].remove(item)
    print(puzzle)