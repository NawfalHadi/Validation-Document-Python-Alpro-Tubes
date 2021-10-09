import sys, docx
import string

from PyQt5.QtWidgets import *

# Imported all fun that i made
import createData_fun
import listData_fun
import compareData_fun
import createUser_fun


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.nim = "default"

        self.setWindowTitle("Document Validation")
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)
        self.setMinimumHeight(110)
        self.setMaximumHeight(110)

        self.menu_layout()

        self.mainLayout = QHBoxLayout()

        self.mainLayout.addLayout(self.menuLayout1)
        self.btn_addData.clicked.connect(self.createUIs)
        self.btn_addUser.clicked.connect(self.createUserUIs)

        self.mainLayout.addLayout(self.menuLayout2)
        self.btn_listData.clicked.connect(self.listUIs)
        self.btn_cekData.clicked.connect(self.checkingUis)

        # self.mainLayout.addLayout(self.menpuuLayout3)

        self.setLayout(self.mainLayout)
        self.show()

    def errorMsg(self, msg, layout):
        self.msg_box = QMessageBox(layout)
        self.msg_box.setText(msg)
        self.msg_box.exec_()

    def menu_layout(self):
        self.btn_addData = QPushButton('Masukkan\n Dokumen')
        self.btn_addUser = QPushButton('Masukkan\n User Baru')
        self.btn_listData = QPushButton('List\n Dokumen')
        self.btn_cekData = QPushButton('Cek\n Dokumen')

        self.menuLayout1 = QVBoxLayout()
        self.menuLayout1.addWidget(self.btn_addData)
        self.menuLayout1.addWidget(self.btn_addUser)

        self.menuLayout2 = QVBoxLayout()
        self.menuLayout2.addWidget(self.btn_listData)
        self.menuLayout2.addWidget(self.btn_cekData)

        # self.menuLayout3 = QVBoxLayout()
        # self.menuLayout3.addWidget(self.btn_cekData)

    # Create Data UI

    def createUIs(self):
        self.createWindow = QMainWindow(self)
        self.createWindow.setMinimumHeight(400)
        self.createWindow.setMaximumHeight(400)
        self.createWindow.setMinimumWidth(500)
        self.createWindow.setMaximumWidth(500)

        # On The Top

        self.text_title = QLabel(self.createWindow)
        self.text_title.setText('Judul :')
        self.text_title.move(18, 25)

        self.input_title = QLineEdit(self.createWindow)
        self.input_title.setText('Judul Dokumen')
        self.input_title.move(65, 25)
        self.input_title.setFixedWidth(400)

        # On The Bottom

        self.text_path = QLabel(self.createWindow)
        self.text_path.setText('PATH :')
        self.text_path.move(18, 270)

        self.dic_name = QLineEdit(self.createWindow)
        self.dic_name.setText("")
        self.dic_name.move(65, 270)
        self.dic_name.setFixedWidth(320)

        self.input_file = QPushButton(self.createWindow)
        self.input_file.move(400, 270)
        self.input_file.setText("Browse...")
        self.input_file.setFixedWidth(80)

        self.input_file.clicked.connect(self.getDic)

        self.submit_file = QPushButton(self.createWindow)
        self.submit_file.move(150, 320)
        self.submit_file.setText("Upload")
        self.submit_file.setFixedWidth(200)

        self.submit_file.clicked.connect(lambda: self.valid_vefCode(self.dic_name.text(), self.input_title.text()))
        self.createWindow.show()

    # Create User UI

    def createUserUIs(self):
        self.cuserLayout = QMainWindow(self)
        self.cuserLayout.setMaximumSize(300, 260)
        self.cuserLayout.setMinimumSize(300, 260)

        self.text_nimUser = QLabel(self.cuserLayout)
        self.text_nimUser.setText("Nim : Maximal Character 7")
        self.text_nimUser.move(10, 10)
        self.text_nimUser.setFixedWidth(300)

        self.input_nimUser = QLineEdit(self.cuserLayout)
        self.input_nimUser.move(10, 40)
        self.input_nimUser.setFixedWidth(280)

        self.text_nameUser = QLabel(self.cuserLayout)
        self.text_nameUser.setText("Name : ")
        self.text_nameUser.move(10, 70)
        self.text_nameUser.setFixedWidth(300)

        self.input_nameUser = QLineEdit(self.cuserLayout)
        self.input_nameUser.move(10, 100)
        self.input_nameUser.setFixedWidth(280)

        self.text_codeUser = QLabel(self.cuserLayout)
        self.text_codeUser.move(10, 130)
        self.text_codeUser.setText("Verify Code : Minimal 4 Character")
        self.text_codeUser.setFixedWidth(300)

        self.input_codeUser = QLineEdit(self.cuserLayout)
        self.input_codeUser.move(10, 160)
        self.input_codeUser.setFixedWidth(280)

        self.btn_newUser = QPushButton(self.cuserLayout)
        self.btn_newUser.setText("Masukkan Data")
        self.btn_newUser.move(10, 200)
        self.btn_newUser.setFixedWidth(280)

        self.btn_newUser.clicked.connect(self.valid_vefAdmin)

        self.cuserLayout.show()

    # Validasi Admin Buat Masukkin Data Ke Info User

    def valid_vefAdmin(self):
        self.vadminLayout = QMainWindow(self)
        self.vadminLayout.setMinimumSize(300, 200)
        self.vadminLayout.setMaximumSize(300, 200)

        self.text_usernameAdmin = QLabel(self.vadminLayout)
        self.text_usernameAdmin.setFixedWidth(300)
        self.text_usernameAdmin.setText("Username : ")
        self.text_usernameAdmin.move(10, 10)

        self.input_usernameAdmin = QLineEdit(self.vadminLayout)
        self.input_usernameAdmin.setFixedWidth(280)
        self.input_usernameAdmin.move(10, 40)

        self.text_vefCodeAdmin = QLabel(self.vadminLayout)
        self.text_vefCodeAdmin.setFixedWidth(300)
        self.text_vefCodeAdmin.setText("Password : ")
        self.text_vefCodeAdmin.move(10, 70)

        self.input_vefCodeAdmin = QLineEdit(self.vadminLayout)
        self.input_vefCodeAdmin.setFixedWidth(280)
        self.input_vefCodeAdmin.move(10, 100)

        self.btn_formAdmin = QPushButton(self.vadminLayout)
        self.btn_formAdmin.setFixedWidth(280)
        self.btn_formAdmin.move(10, 140)
        self.btn_formAdmin.setText("Submit Data")

        self.btn_formAdmin.clicked.connect(lambda: self.verifingAdmin(self.input_usernameAdmin.text().lower(),
                                                                      self.input_vefCodeAdmin.text().lower()))

        lengthNim = len(self.input_nimUser.text())
        validationLength = 0
        for i in range(lengthNim):
            if self.input_nimUser.text()[i] in string.digits:
                validationLength += 1

        if len(self.input_nimUser.text().strip()) < 5 or len(self.input_nimUser.text().strip()) > 8 or \
                len(self.input_codeUser.text()) < 4 or validationLength != lengthNim:
            self.errorMsg("Salah memasukkan NIM atau kurang memasukkan code", self.vadminLayout)
            self.vadminLayout.close()
        else:
            self.vadminLayout.show()

    # Validasi Vef Code

    def valid_vefCode(self, path, title):
        self.vefLayout = QMainWindow(self)
        self.vefLayout.setMinimumWidth(500)
        self.vefLayout.setMaximumWidth(500)
        self.vefLayout.setMinimumHeight(120)
        self.vefLayout.setMaximumHeight(120)

        self.text_vef = QLabel(self.vefLayout)
        self.text_vef.setText('Verify Your Code')
        self.text_vef.move(200, 15)

        self.text_vef = QLabel(self.vefLayout)
        self.text_vef.setText('Verification Code :')
        self.text_vef.move(18, 55)

        self.input_vef = QLineEdit(self.vefLayout)
        self.input_vef.setText('Judul Dokumen')
        self.input_vef.move(125, 55)
        self.input_vef.setFixedWidth(265)

        self.btn_vef = QPushButton(self.vefLayout)
        self.btn_vef.setText("Verif")
        self.btn_vef.move(400, 55)
        self.btn_vef.setFixedWidth(80)

        # Code ======

        if path == "" or len(path) < 6:
            self.errorMsg("Masukkan File Terlebih Dahulu", self.createWindow)
            self.vefLayout.close()
        elif "docx" not in path:
            self.errorMsg("Harus menggunakan File .docx", self.createWindow)
        elif path != "":
            if self.input_title.text() == "":
                self.errorMsg("Masukkan Judul Yang Ada Di Dokumen", self.createWindow)
            else:
                gate1 = createData_fun.searchNim(self, path)
                if gate1[0] == 0:
                    self.errorMsg(gate1[1], self.createWindow)
                else:
                    doc = docx.Document(path).paragraphs
                    gate2 = createData_fun.searchTitle(self, self.input_title.text(), doc)
                    if gate2[0] == 0:
                        self.errorMsg(gate2[1], self.errorMsg())
                    elif gate2[0] == 1:
                        print(gate2)
                        tempNim = createData_fun.getNim(path)
                        print("Bismillah")
                        self.btn_vef.clicked.connect(lambda: self.vef_codew(title, tempNim, path))
                        print(tempNim)
                        self.vefLayout.show()

        # Bismillah work :"D

        # Code ======

    # Start Of List UI

    def listUIs(self):
        self.listWindow = QMainWindow(self)
        self.listWindow.setMinimumWidth(510)
        self.listWindow.setMaximumWidth(510)
        self.listWindow.setMinimumHeight(530)
        self.listWindow.setMaximumHeight(530)

        # ======================
        # Center ===============
        # ======================

        self.text_searchDoc = QLabel(self.listWindow)
        self.text_searchDoc.setText('NIM :')
        self.text_searchDoc.move(18, 25)

        self.input_searchDoc = QLineEdit(self.listWindow)
        self.input_searchDoc.setText(f'{self.nim}')
        self.input_searchDoc.move(65, 25)
        self.input_searchDoc.setFixedWidth(320)

        self.btn_searchDoc = QPushButton(self.listWindow)
        self.btn_searchDoc.setText("Search")
        self.btn_searchDoc.move(400, 25)
        self.btn_searchDoc.setFixedWidth(80)
        self.btn_searchDoc.clicked.connect(self.getNim)

        self.btn_infoUser = QPushButton(self.listWindow)
        self.btn_infoUser.setText("Info Mahasiswa")
        self.btn_infoUser.move(5, 490)
        self.btn_infoUser.setFixedWidth(500)
        self.btn_infoUser.clicked.connect(lambda: self.getInfo(self.nim))

        # ======================
        # Below ===============
        # ======================

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox(f"Dokumen {self.nim}")
        self.btn_info = QPushButton

        with open(f"Data/User/{self.nim}.txt", 'r') as nim:
            for i in nim:
                temp = i.split(',')
                slashN = temp[1][0:len(temp[1]) - 1]
                self.formLayout.addRow(QLabel(temp[0]), QLabel(f'| {slashN}'))

        self.groupBox.setLayout(self.formLayout)
        self.groupBox.setMinimumWidth(490)
        self.scroll = QScrollArea(self.listWindow)
        self.scroll.setWidget(self.groupBox)
        self.scroll.setMinimumWidth(500)
        self.scroll.setMinimumHeight(400)
        self.scroll.move(5, 70)

        self.listWindow.show()

    # Info Mahasiswa

    def infoWindow(self, nim, name, prodi, status):
        self.infomahasiswaLayout = QMainWindow()
        self.infomahasiswaLayout.setWindowTitle(f'Data {status} {nim}')
        self.infomahasiswaLayout.setMinimumSize(250, 130)
        self.infomahasiswaLayout.setMaximumSize(250, 130)

        self.infoNim = QLabel(self.infomahasiswaLayout)
        self.infoNim.setText(nim)
        self.infoNim.move(10, 10)

        self.infoName = QLabel(self.infomahasiswaLayout)
        self.infoName.setText(f'Name : {name}')
        self.infoName.setFixedWidth(300)
        self.infoName.move(10, 40)

        self.infoProdi = QLabel(self.infomahasiswaLayout)
        self.infoProdi.setText(f'Prodi : {prodi}')
        self.infoProdi.setFixedWidth(300)
        self.infoProdi.move(10, 70)

        self.infoStatus = QLabel(self.infomahasiswaLayout)
        self.infoStatus.setText(f'Status : {status}')
        self.infoStatus.setFixedWidth(300)
        self.infoStatus.move(10, 100)

        if nim == 'default':
            self.errorMsg("Masukkan NIM yang ada di Database", self.listWindow)
            self.infomahasiswaLayout.close()
        else:
            self.infomahasiswaLayout.show()

    def checkingUis(self):
        self.checkingLayout = QMainWindow(self)
        self.checkingLayout.setMinimumWidth(920)
        self.checkingLayout.setMaximumWidth(920)
        self.checkingLayout.setMinimumHeight(330)
        self.checkingLayout.setMaximumHeight(330)

        # Left Section

        self.text_dicL = QLabel(self.checkingLayout)
        self.text_dicL.setText("C:/.../fileName.docx")
        self.text_dicL.move(30, 259)
        self.text_dicL.setFixedWidth(1000)

        self.btn_dicL = QPushButton(self.checkingLayout)
        self.btn_dicL.setText("Search")
        self.btn_dicL.move(325, 260)

        # Right Section

        self.dic_get = QLineEdit(self.checkingLayout)
        self.dic_get.setText('C:/...')
        self.dic_get.move(438, 260)
        self.dic_get.setFixedWidth(365)

        self.text_dic = QLabel(self.checkingLayout)
        self.text_dic.setText("fileName.docx")
        self.text_dic.move(580, 225)
        self.text_dic.setFixedWidth(1000)

        self.btn_dic = QPushButton(self.checkingLayout)
        self.btn_dic.setText("Get File")
        self.btn_dic.move(810, 260)
        self.btn_dic.clicked.connect(self.getDic2)

        self.checkingLayout.show()

    # All Function
    # Create Function

    def getDic(self):
        createData_fun.getDic(self, self.createWindow, self.dic_name)

    def vef_codew(self, title, nim, path):
        wait = createData_fun.movingFile(self, title, nim, path)
        if wait[0] == 0:
            self.errorMsg(wait[1], self.createWindow)
        else:
            self.errorMsg(wait[1], self.createWindow)
            self.vefLayout.close()
            self.createWindow.close()

    # List Function

    def getNim(self):
        listData_fun.getList(self, self.listWindow, self.nim, self.input_searchDoc)
        self.listUIs()

    def getInfo(self, nims):
        data = listData_fun.getNim(self, nims)
        print(data)
        if data[0] == 0:
            self.errorMsg(data[1], self.listWindow)
        else:
            self.infoWindow(data[0], data[1], data[3], data[4])

    # Compare Function

    def getDic2(self):
        createData_fun.getDic(self, self.checkingLayout, self.dic_get)
        getNameFile = self.dic_get.text().split('/')
        self.text_dic.setText(getNameFile[len(getNameFile) - 1])

        doc = docx.Document(self.dic_get.text()).paragraphs
        nimCheck = compareData_fun.searchNim(self, doc)
        print(nimCheck)
        titleCheck = compareData_fun.searchTitle(self, nimCheck, doc)
        print(titleCheck)
        fileCheck = compareData_fun.getFileDB(self, nimCheck, titleCheck)
        self.text_dicL.setText(fileCheck.split(",")[0])
        fileDbPath = docx.Document(f'Data/File/{nimCheck}/{fileCheck.split(",")[0]}').paragraphs
        presentase = compareData_fun.comparing(self, doc, fileDbPath)
        self.errorMsg(presentase, self.checkingLayout)

    # admin verification Function

    def verifingAdmin(self, usernm, passw):
        status = createUser_fun.verification(self, usernm, passw)
        message = ""
        if status == "succes":
            checkNim = createUser_fun.checkingNim(self, self.input_nimUser.text())
            print('allhamdulillah')
            if checkNim[0] == 0:
                self.errorMsg("Nim sudah ada / Salah memasukkan format\n cek tahun"
                              "dan kode prodi", self.vadminLayout)
            else:
                create = createUser_fun.sendToDb(self, checkNim[0], self.input_nameUser.text(),
                                                 self.input_codeUser.text(), checkNim[1])
                print(create)
                self.vadminLayout.close()
                self.cuserLayout.close()
        else:
            message = "failed"
            self.errorMsg("Salah masukkan password/username", self.vadminLayout)

        print(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())
