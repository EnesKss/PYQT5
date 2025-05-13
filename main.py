import sys
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Örneği") #uygulamanın başlığı
        label = QLabel("Merhaba PyQt!")  #ekranda çıkan yazı 
        self.setCentralWidget(label)   #ana pencere

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())