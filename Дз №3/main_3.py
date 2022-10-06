dic = {}


with open(r"Дз №3\sorted\1.txt", "rt", encoding="utf8") as file:
    place = r"Дз №3\sorted\1.txt"
    name_file = "1.txt"
    lines = 0
    for line in file:
        lines += 1
    dic[place] = [lines, name_file]


with open(r"Дз №3\sorted\2.txt", "rt", encoding="utf8") as file:
    place = r"Дз №3\sorted\2.txt"
    name_file = "2.txt"
    lines = 0
    for line in file:
        lines += 1
    dic[place] = [lines, name_file]


with open(r"Дз №3\sorted\3.txt", "rt", encoding="utf8") as file:
    place = r"Дз №3\sorted\3.txt"
    name_file = "3.txt"
    lines = 0
    for line in file:
        lines += 1
        dic[place] = [lines, name_file]


sort_dic = dict(sorted(dic.items(), key=lambda x: x[1][0]))


with open(r"Дз №3\sorted\new_file.txt", "at", encoding="utf8") as file:
    for num, place in enumerate(sort_dic):
        text = open(place, "rt", encoding="utf8")
        file.write(f"{sort_dic[place][1]}\n")
        file.write(str(f"{num + 1}\n"))
        file.write(f"{text.read()}\n")
        text.close()




