import sys
from PyQt5 import QtWidgets as qtw
from Gui import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime

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
        if name.isdigit():
            error_message = "Error: Name cannot be a numeric value."
            QMessageBox.warning(self, "Validation Error", error_message)
            return
        elif len(name)==0:
            error_message="The name field cannot be left blank"
            QMessageBox.warning(self, "Validation Error", error_message)
            return

        surname=self.ui.surname.text()
        if surname.isdigit():
            error_message= "Error: Surname cannot be a numeric value."
            QMessageBox.warning(self,"Validation Error",error_message)
            return
        elif len(surname)==0:
            error_message="The surname field cannot be left blank"
            QMessageBox.warning(self, "Validation Error", error_message)
            return
        
        idno=self.ui.idno.text()
        if len(idno)==0:
            error_message="The ID No field cannot be left blank"
            QMessageBox.warning(self, "Validation Error", error_message)
            return
        elif len(idno)!=11:
            error_message= "Error: ID No must be a 11 number"
            QMessageBox.warning(self,"Validation Error",error_message)
            return
        elif not idno.isdigit():
            error_message= "Error: ID No cannot be a string value"
            QMessageBox.warning(self,"Validation Error",error_message)
            return
        
        gender=self.ui.gender.findChildren(qtw.QRadioButton)
        selected_gender=None
        for i in gender:
            if i.isChecked():
                selected_gender=i.text()
                break
        if selected_gender is None:
            QMessageBox.warning(self,"Validation Error","Gender must be selected")
            return

        edtype=self.ui.edtype.findChildren(qtw.QRadioButton)
        selected_edtype=None
        for i in edtype:
            if i.isChecked():
                selected_edtype=i.text()
                break
        if selected_edtype is None:
            QMessageBox.warning(self,"Validation Error","Education Type must be selected")
            return

        birthplace=self.ui.birthplace.currentText()
        if birthplace=="Select":
            QMessageBox.warning(self,"Validation Error","Please select your place of birth")
            return
        
        studydep=self.ui.studydep.currentText()
        if studydep=="Select":
            QMessageBox.warning(self,"Validation Error","Please select the department you are studying")
            return

        birthdate=self.ui.birthdate.selectedDate().toString("dd-MM-yyyy")
        current_year=datetime.now().year
        years_old=current_year-int(birthdate[-4:])
        
        if years_old<18 or years_old>100:
            QMessageBox.warning(self,"Validation Error","Please select a valid date")
            return 

        rowcount=self.ui.tableWidget.rowCount()-1

        self.ui.tableWidget.setItem(rowcount,0,QTableWidgetItem(name))
        self.ui.tableWidget.setItem(rowcount,1,QTableWidgetItem(surname))
        self.ui.tableWidget.setItem(rowcount,2,QTableWidgetItem(idno))
        self.ui.tableWidget.setItem(rowcount,3,QTableWidgetItem(birthplace))
        self.ui.tableWidget.setItem(rowcount,4,QTableWidgetItem(studydep))
        self.ui.tableWidget.setItem(rowcount,5,QTableWidgetItem(birthdate))
        self.ui.tableWidget.setItem(rowcount,6,QTableWidgetItem(selected_gender))
        self.ui.tableWidget.setItem(rowcount,7,QTableWidgetItem(selected_edtype))

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