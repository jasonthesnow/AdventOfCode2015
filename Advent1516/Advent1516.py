children = 3
cats = 7
samoyeds = 2
pomeranians = 3
akitas = 0
vizslas = 0
goldfish = 5
trees = 3
cars = 2
perfumes = 1

sue_info = dict()
sue_match = dict()

with open("input.txt") as f:
    for line in f:
        word = line.split()
        current_sue = int(word[1].strip(":"))
        
        sue_match[current_sue] = True

        sue_info[current_sue] = {}
        sue_info[current_sue][word[2].strip(":")] = int(word[3].strip(","))
        sue_info[current_sue][word[4].strip(":")] = int(word[5].strip(","))
        sue_info[current_sue][word[6].strip(":")] = int(word[7].strip(","))

for i in range(len(sue_match)):
    try:
        if not sue_info[i + 1]["children"] == children:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["cats"] > cats:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["samoyeds"] == samoyeds:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["pomeranians"] < pomeranians:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["akitas"] == akitas:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["vizslas"] == vizslas:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["goldfish"] < goldfish:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["trees"] > trees:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["cars"] == cars:
            sue_match[i + 1] = False
    except KeyError:
        pass

    try:
        if not sue_info[i + 1]["perfumes"] == perfumes:
            sue_match[i + 1] = False
    except KeyError:
        pass

    if sue_match[i + 1]:
        print(i + 1)

