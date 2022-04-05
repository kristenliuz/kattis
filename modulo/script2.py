

bag = []

for i in range(10):
    enterNum = int(input())
  
    modulo = enterNum%42
    bag.append(modulo)


def kristenunique (list):
    fetch_unique = []

    for u in bag:
        if u not in fetch_unique:
            fetch_unique.append(u)
    
    print(len(fetch_unique))

kristenunique(bag)