from PyQt5.QtWidgets import *
import datetime


def verification(self, usernm, passw):
    if usernm == "admin" and passw == "admin":
        return "succes"
    else:
        return "failed"


def prodiChecking(nim):
    prodi = ''

    if len(nim) == 7:
        with open('Data/infoProdi.txt', 'r') as prods:
            for prodih in prods:
                if nim[0] in prodih:
                    prodi = prodih.split(',')[1]
                    break
                else:
                    prodi = [0, f"Tidak ada prodi {nim[0:2]}"]
        return prodi

    elif len(nim) == 8:
        with open('Data/infoProdi.txt', 'r') as prods:
            for prodih in prods:
                if nim[0:2] in prodih:
                    prodi = prodih.split(',')[1]
                    break
                else:
                    prodi = [0, f"Tidak ada prodi {nim[0:2]}"]
        return prodi


def yearChecking(nim):
    year = datetime.datetime.now().strftime("%y")

    if len(nim) == 7:
        if int(nim[1:3]) <= int(year):
            return nim[1:3]
        else:
            print(f"ini masih tahun {datetime.datetime.now().strftime('%Y')}")
            return "failed"

    elif len(nim) == 8:
        if int(nim[2:4]) <= int(year):
            return nim[2:4]
        else:
            print(f"ini masih tahun {datetime.datetime.now().strftime('%Y')}")
            return "failed"


def checkingNim(self, nim):
    tempNim = []
    message = 0
    prodi = ''
    with open('Data/infoUser.txt', 'r') as nima:
        for nims in nima:
            tempNim.append(nims.split(",")[0])

    if nim not in tempNim:
        message = 1
    else:
        message = 0

    if message == 1:
        prodi = prodiChecking(nim)
        if prodi[0] == 0:
            return prodi[1]
        year = yearChecking(nim)
        if year == 'failed':
            return [0, f"ini masih tahun {datetime.datetime.now().strftime('%Y')}"]
        return [nim, f"{prodi[0:len(prodi) - 1]}'{year}"]
    else:
        return [0, 'nim sudah ada di dalam database']


def sendToDb(self, nim, name, passw, prodi, status='mahasiswa'):
    validating = 0
    with open('Data/infoUser.txt', 'r') as userR:
        for i in userR:
            validating += 1

    with open('Data/infoUser.txt', 'a') as users:
        if validating != 0:
            users.write(f'\n{nim},{name},{passw},{prodi},{status}')
        elif validating == 0:
            users.write(f'{nim},{name},{passw},{prodi},{status}')

    with open(f'Data/User/{nim}.txt', 'w') as newUser:
        return "Succecfull"
