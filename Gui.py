from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 790)
        MainWindow.setMinimumSize(QtCore.QSize(1098, 790))
        MainWindow.setMaximumSize(QtCore.QSize(1098, 790))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1098, 790))
        self.centralwidget.setMaximumSize(QtCore.QSize(1098, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(-60, -20, 1381, 841))
        self.label.setMinimumSize(QtCore.QSize(1381, 841))
        self.label.setMaximumSize(QtCore.QSize(1383, 841))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("kizkulesi.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 90, 291, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 10, 171, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.surname = QtWidgets.QLineEdit(self.layoutWidget)
        self.surname.setObjectName("surname")
        self.verticalLayout.addWidget(self.surname)
        self.idno = QtWidgets.QLineEdit(self.layoutWidget)
        self.idno.setObjectName("idno")
        self.verticalLayout.addWidget(self.idno)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 90, 261, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(100, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.birthplace = QtWidgets.QComboBox(self.frame_2)
        self.birthplace.setGeometry(QtCore.QRect(50, 40, 191, 22))
        self.birthplace.setObjectName("birthplace")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(330, 170, 301, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(60, 0, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.studydep = QtWidgets.QComboBox(self.frame_3)
        self.studydep.setGeometry(QtCore.QRect(40, 30, 221, 21))
        self.studydep.setObjectName("studydep")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(790, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.birthdate = QtWidgets.QCalendarWidget(self.centralwidget)
        self.birthdate.setGeometry(QtCore.QRect(670, 130, 376, 218))
        self.birthdate.setObjectName("birthdate")
        self.gender = QtWidgets.QGroupBox(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(10, 260, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gender.setFont(font)
        self.gender.setFlat(False)
        self.gender.setObjectName("gender")
        self.male = QtWidgets.QRadioButton(self.gender)
        self.male.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.male.setObjectName("male")
        self.female = QtWidgets.QRadioButton(self.gender)
        self.female.setGeometry(QtCore.QRect(20, 60, 95, 20))
        self.female.setObjectName("female")
        self.edtype = QtWidgets.QGroupBox(self.centralwidget)
        self.edtype.setGeometry(QtCore.QRect(300, 260, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.edtype.setFont(font)
        self.edtype.setObjectName("edtype")
        self.formal = QtWidgets.QRadioButton(self.edtype)
        self.formal.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.formal.setObjectName("formal")
        self.second = QtWidgets.QRadioButton(self.edtype)
        self.second.setGeometry(QtCore.QRect(20, 60, 221, 20))
        self.second.setObjectName("second")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(180, 370, 701, 80))
        self.frame_4.setMaximumSize(QtCore.QSize(1383, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.addreg = QtWidgets.QPushButton(self.frame_4)
        self.addreg.setGeometry(QtCore.QRect(50, 27, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.addreg.setFont(font)
        self.addreg.setObjectName("addreg")
        self.delreg = QtWidgets.QPushButton(self.frame_4)
        self.delreg.setGeometry(QtCore.QRect(370, 27, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.delreg.setFont(font)
        self.delreg.setObjectName("delreg")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 530, 1101, 261))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hoşgeldiniz"))
        self.label_2.setText(_translate("MainWindow", "Student Registration System"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Surname"))
        self.label_5.setText(_translate("MainWindow", "ID No"))
        self.label_6.setText(_translate("MainWindow", "Birthplace"))
        self.label_8.setText(_translate("MainWindow", "Department of Study"))
        self.label_9.setText(_translate("MainWindow", "Date of Birth"))
        self.gender.setTitle(_translate("MainWindow", "Gender"))
        self.male.setText(_translate("MainWindow", "Male"))
        self.female.setText(_translate("MainWindow", "Female"))
        self.edtype.setTitle(_translate("MainWindow", "Education Type"))
        self.formal.setText(_translate("MainWindow", "Formal"))
        self.second.setText(_translate("MainWindow", "Secondary Education"))
        self.addreg.setText(_translate("MainWindow", "Add Registration"))
        self.delreg.setText(_translate("MainWindow", "Delete Registration"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID No"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Birthplace"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Department"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Birthdate"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Education"))
