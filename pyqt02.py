#grid düzen verme (GridLayout), PushButton ekleme
from PyQt5.QtWidgets import * # PyQt5.QtWidgets modülünden tüm sınıfları getir 
from PyQt5.QtGui import QIcon  # her hangi bir icon eklemek için
import sys 

class Mywindow(QWidget): # Qwidget sınıfından miras al 
    def __init__(self): # kurucu fonksiyon
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Diyalog Penceresi")
        usernameLabel=QLabel("&Username",self) 
        usernameTBox=QLineEdit(self)
        usernameLabel.setBuddy(usernameTBox) 

        passLabel=QLabel("&Password",self) 
        passTBox=QLineEdit(self)
        passLabel.setBuddy(passTBox) # setBuddy metodu iki tane widget i ilişkilendirmek 
        #için kullanılır
        btOk=QPushButton("&Ok")
        btnCancel=QPushButton("&Cancel")
        grid=QGridLayout() # layout yerleşim düzeni tanımla yerleşim olarak grid
        grid.addWidget(usernameLabel,0,0) # bu yerleşim düzeninin içine oluşturduğum araçları ekle
        grid.addWidget(usernameTBox,0,1,1,2)
        grid.addWidget(passLabel,1,0) # bu yerleşim düzeninin içine oluşturduğum araçları ekle
        grid.addWidget(passTBox,1,1,1,2)
        grid.addWidget(btOk,2,1)
        grid.addWidget(btnCancel,2,2)
        # grid.addWidget(passTBox)
        self.setLayout(grid)







if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Mywindow()
    win.show()
    sys.exit(app.exec_())