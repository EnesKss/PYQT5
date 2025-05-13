from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 10, 751, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Göster"))
        self.pushButton.clicked.connect(self.goster)
    def goster(self):
        try:
            client=MongoClient("localhost:27017")
            client.admin.command("ping") # MongoDB sunucusu kontrol et
            QtWidgets.QMessageBox.information(None, "Bağlantı","Bağlantı yapıldı")
            db=client["Okul"]
            coll=db["ogrenciler"]
            ogrenciler=coll.find({},{"_id":0})
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Ad","Soyadı","Yaşı","Cinsiyeti"])
            
            for a in ogrenciler:
                name=a.get("name","Bilinmeyen")
                surname=a.get("surname","Bilinmeyen")
                age=a.get("age","Bilinmeyen")
                gender=a.get("gender","Bilinmeyen")
                row_position=self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position,0, QtWidgets.QTableWidgetItem(name))
                self.tableWidget.setItem(row_position,1, QtWidgets.QTableWidgetItem(surname))
                self.tableWidget.setItem(row_position,2, QtWidgets.QTableWidgetItem(age))
                self.tableWidget.setItem(row_position,3, QtWidgets.QTableWidgetItem(gender))
            
            
        except Exception as e:
            QtWidgets.QMessageBox.information(None, "Bağlantı", str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
