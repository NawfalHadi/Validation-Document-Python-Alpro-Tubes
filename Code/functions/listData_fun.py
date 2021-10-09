from PyQt5.QtWidgets import *


def getList(self, windowApp, nim, nimG):
    windowApp.close()
    self.nim = nimG.text()
    tempList = []
    with open('Data/infoUser.txt') as user:
        for i in user:
            temp = i.split(',')
            tempList.append(temp[0])
    if self.nim in tempList:
        self.nim = self.nim
    else:
        self.nim = 'default'


def getNim(self, nim):
    if nim == 'default':
        return [0, 'Tidak mendapatkan nim yang valid']

    temp = []
    with open('Data/infoUser.txt', 'r') as dataUser:
        for nims in dataUser:
            temp.append(nims.split(',')[0])

    for i in temp:
        if nim == i:
            with open('Data/infoUser.txt', 'r') as dataUser2:
                for nims2 in dataUser2:
                    if nim == nims2.split(',')[0]:
                        return nims2.split(',')
