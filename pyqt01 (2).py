#Temel iki widget (label) ekleme, dikey düzen verme (vboxlayout)
from PyQt5.QtWidgets import * # PyQt5.QtWidgets modülünden tüm sınıfları getir 
from PyQt5.QtGui import QIcon  # her hangi bir icon eklemek için
import sys 

class Mywindow(QWidget): # Qwidget sınıfından miras al 
    def __init__(self): # kurucu fonksiyon
        super().__init__()
        self.initGUI()

    def initGUI(self):
        label1=QLabel(self) #Label oluşturmak için 
        label1.setText("Label1") # label a bir string atamak için kullanılır 
        label2=QLabel(self)
        label2.setText("Label2")
        vbox=QVBoxLayout() # layout yerleşim düzeni tanımla
        vbox.addWidget(label1) # bu yerleşim düzeninin içine oluşturduğum araçları ekle
        vbox.addWidget(label2)
        self.setLayout(vbox)







if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Mywindow()
    win.show()
    sys.exit(app.exec_())