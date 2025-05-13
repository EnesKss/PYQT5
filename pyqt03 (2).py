#grid düzen verme (GridLayout), PushButton ekleme
from PyQt5.QtWidgets import * # PyQt5.QtWidgets modülünden tüm sınıfları getir 
from PyQt5.QtGui import QIcon  # her hangi bir icon eklemek için
import sys 

class Mywindow(QWidget): # Qwidget sınıfından miras al 
    def __init__(self): # kurucu fonksiyon
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Push Button örneği")
        self.setGeometry(1200, 100, 400, 400) # x,y,w,h
        self.closeButton=QPushButton(self)
        self.closeButton.setShortcut("Ctrl+C") # widget için kısayol atama
        self.closeButton.resize(100,100) # widget boyutunu değiştirmek w,h
        # self.closeButton.clicked.connect(self.close) # direk olayı burada kullanabilirsiniz
        self.closeButton.clicked.connect(self.fnClose) # fonksiyon burada çağrılır 
    def fnClose(self): #bir fonksiyon içinde tanımlarız ve event i buradan çağırırız
        print("buton kapatıldı")
        self.close()







if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Mywindow()
    win.show()
    sys.exit(app.exec_())