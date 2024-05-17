import sys
from PyQt5 import QtWidgets as qtw
from Gui import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem

class App(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.birthplace.addItems(["Select","Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"])
        self.ui.studydep.addItems(["Select","Archeology","Astronomy","Computer Engineering","Biochemistry","Biology","Geography","Economics","Electrical Engineering","Industrail Engineering","Philosopyh","Finance","Physics","Nursing","Civil Engineering","Statistics","Chemistry","Mechanical Engineering","Mathematics","Architecture","Psychology","History","Theatre","Zoology"])

        self.ui.addreg.clicked.connect(self.register)
        self.ui.delreg.clicked.connect(self.deletereg)

    def register(self):
        name=self.ui.name.text()
        surname=self.ui.surname.text()
        idno=self.ui.idno.text()
        
        gender=self.ui.gender.findChildren(qtw.QRadioButton)
        for i in gender:
            if i.isChecked():
                sex=i.text()
        edtype=self.ui.edtype.findChildren(qtw.QRadioButton)
        for i in edtype:
            if i.isChecked():
                education=i.text()
        
        birthplace=self.ui.birthplace.currentText()
        studydep=self.ui.studydep.currentText()
        birthdate=self.ui.birthdate.selectedDate().toString("dd-MM-yyyy")

        rowcount=self.ui.tableWidget.rowCount()-1

        self.ui.tableWidget.setItem(rowcount,0,QTableWidgetItem(name))
        self.ui.tableWidget.setItem(rowcount,1,QTableWidgetItem(surname))
        self.ui.tableWidget.setItem(rowcount,2,QTableWidgetItem(idno))
        self.ui.tableWidget.setItem(rowcount,3,QTableWidgetItem(birthplace))
        self.ui.tableWidget.setItem(rowcount,4,QTableWidgetItem(studydep))
        self.ui.tableWidget.setItem(rowcount,5,QTableWidgetItem(birthdate))
        self.ui.tableWidget.setItem(rowcount,6,QTableWidgetItem(sex))
        self.ui.tableWidget.setItem(rowcount,7,QTableWidgetItem(education))

        self.ui.tableWidget.insertRow(rowcount+1)

    def deletereg(self):
        selected=self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(selected)


def runner():
    applic=qtw.QApplication(sys.argv)
    win=App()
    win.show()
    sys.exit(applic.exec_())
runner()