from PyQt5.QtWidgets import *


def searchNim(self, paragraphs):
    print("Nimming...")
    tempList = []
    with open('Data/infoUser.txt') as user:
        for nim in user:
            temp = nim.split(',')
            tempList.append(temp[0])

    tempSort = sorted(tempList)
    for nims in tempSort:
        for i in range(len(paragraphs)):
            if nims in paragraphs[i].text:
                return nims


def searchTitle(self, nim, parag):
    tempTitle = []
    with open(f'Data/User/{nim}.txt', 'r') as titling:
        for a in titling:
            tempTitle.append(a.split(',')[0])
        print(tempTitle)

    sortSelish = []
    for b in tempTitle:
        splitingTitle = b.split("_")[0]
        splitText = splitingTitle.split()
        print(splitText)

        dif = 0  # Selisih
        if len(parag) > 15:
            cntr = 0
            for i in range(16):
                while True:
                    if cntr >= len(parag):
                        break
                    if len(parag[cntr].text) > 0:
                        for j in splitText:
                            if j.lower() in parag[cntr].text.lower():
                                dif += 1
                                print(dif)
                                sortSelish.append([dif, splitingTitle])
                        cntr += 1
                        break
                    else:
                        cntr += 1
                if cntr > len(parag):
                    break
        else:
            cntr = 0
            for g in parag:
                while True:
                    if cntr >= len(parag):
                        break
                    if len(parag[cntr].text) > 0:
                        for k in splitText:
                            if k.lower() in parag[cntr].text.lower():
                                dif += 1
                                print(dif)
                                sortSelish.append([dif, splitingTitle])
                        cntr += 1
                        break
                    else:
                        cntr += 1
                if cntr > len(parag):
                    break
    sorting = sorted(sortSelish)
    return sorting[len(sorting) - 1][1]


def getFileDB(self, nim, title):
    with open(f'Data/User/{nim}.txt', 'r') as titles:
        for i in titles:
            if title in i:
                return i


def comparing(self, fileOutside, fileDb):
    insideDb = []
    OutsideDb = []

    for inside in fileDb:
        if len(inside.text) > 0:
            temp = inside.text
            insideDb.append(temp.split())
        else:
            pass

    for outside in fileOutside:
        if len(outside.text) > 0:
            tempO = outside.text
            OutsideDb.append(tempO.split())
        else:
            pass

    total = 0
    trues = 0
    falses = 0

    for parag in range(len(insideDb)):
        for words in range(len(insideDb[parag])):
            if len(insideDb[parag]) > 0:
                try:
                    if OutsideDb[parag][words] in insideDb[parag]:
                        insideDb[parag].pop(0)
                        total += 1
                        trues += 1
                    else:
                        total += 1
                        falses += 1
                except IndexError:
                    falses += 1
                    total += 1
                    print("astaghfirullah")
            else:
                break
    print(insideDb)
    print("allhamdulillah")

    print(int(((trues - falses)/total)*100))
    return f"Presentase Validasi File : {int(((trues - falses)/total)*100)}%"


