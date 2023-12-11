
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
import os 
script_directory = os.path.dirname(os.path.realpath(__file__))


os.chdir(script_directory)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 619)
        icon_path = os.path.join(script_directory, "hesapicon.png")
        icon = QtGui.QIcon(icon_path)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(330, 70, 311, 471))
        self.groupBox.setObjectName("groupBox")
        self.sonucText = QtWidgets.QLabel(self.groupBox)
        self.sonucText.setGeometry(QtCore.QRect(10, 180, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        self.sonucText.setFont(font)
        self.sonucText.setObjectName("sonucText")
        self.sonucText.setStyleSheet("color: green;")
        self.bugunkuDBtn = QtWidgets.QPushButton(self.groupBox)
        self.bugunkuDBtn.setGeometry(QtCore.QRect(20, 390, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.bugunkuDBtn.setFont(font)
        self.bugunkuDBtn.setObjectName("bugunkuDBtn")
        self.bilesikFaizBtn = QtWidgets.QPushButton(self.groupBox)
        self.bilesikFaizBtn.setGeometry(QtCore.QRect(20, 290, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.bilesikFaizBtn.setFont(font)
        self.bilesikFaizBtn.setObjectName("bilesikFaizBtn")
        self.gelecekDBtn = QtWidgets.QPushButton(self.groupBox)
        self.gelecekDBtn.setGeometry(QtCore.QRect(20, 340, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.gelecekDBtn.setFont(font)
        self.gelecekDBtn.setObjectName("gelecekDBtn")
        self.basitFaizBtn = QtWidgets.QPushButton(self.groupBox)
        self.basitFaizBtn.setGeometry(QtCore.QRect(20, 240, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.basitFaizBtn.setFont(font)
        self.basitFaizBtn.setObjectName("basitFaizBtn")
        self.formulLbl = QtWidgets.QLabel(self.groupBox)
        self.formulLbl.setGeometry(QtCore.QRect(20, 30, 261, 151))
        self.formulLbl.setObjectName("formulLbl")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 311, 471))
        self.groupBox_2.setObjectName("groupBox_2")
        self.vadeText = QtWidgets.QTextEdit(self.groupBox_2)
        self.vadeText.setGeometry(QtCore.QRect(20, 400, 271, 41))
        self.vadeText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vadeText.setObjectName("vadeText")
        self.vadeText.setText("0")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 370, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.paraText = QtWidgets.QTextEdit(self.groupBox_2)
        self.paraText.setGeometry(QtCore.QRect(20, 60, 271, 41))
        self.paraText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.paraText.setObjectName("paraText")
        self.paraText.setText("0")
        self.taksitText = QtWidgets.QTextEdit(self.groupBox_2)
        self.taksitText.setGeometry(QtCore.QRect(20, 320, 271, 41))
        self.taksitText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taksitText.setObjectName("taksitText")
        self.taksitText.setText("0")
        self.faizText = QtWidgets.QTextEdit(self.groupBox_2)
        self.faizText.setGeometry(QtCore.QRect(20, 150, 271, 41))
        self.faizText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faizText.setObjectName("faizText")
        self.faizText.setText("0")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.zamanText = QtWidgets.QTextEdit(self.groupBox_2)
        self.zamanText.setGeometry(QtCore.QRect(20, 230, 271, 41))
        self.zamanText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zamanText.setObjectName("zamanText")
        self.zamanText.setText("0")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(14, 525, 621, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finansal Hesap Makinesi v0.1"))
        self.label.setText(_translate("MainWindow", "Finansal Hesap Makinesi"))
        self.groupBox.setTitle(_translate("MainWindow", "Sonuç"))
        self.sonucText.setText(_translate("MainWindow", ""))
        self.bugunkuDBtn.setText(_translate("MainWindow", "Bugünkü Değer Anüite Hesapla"))
        self.bilesikFaizBtn.setText(_translate("MainWindow", "Bileşik Faiz Hesapla"))
        self.gelecekDBtn.setText(_translate("MainWindow", "Gelecek Değer Anüite Hesapla"))
        self.basitFaizBtn.setText(_translate("MainWindow", "Basit Faiz Hesapla"))
        self.formulLbl.setText(_translate("MainWindow", ""))
        self.groupBox_2.setTitle(_translate("MainWindow", "Değişkenler"))
        self.label_11.setText(_translate("MainWindow", "Vade (Ay):"))
        self.label_3.setText(_translate("MainWindow", "Faiz Oranı (%):"))
        self.label_4.setText(_translate("MainWindow", "Ödeme (Taksit) Tutarı:"))
        self.label_2.setText(_translate("MainWindow", "Başlangıç Tutarı:"))
        self.label_5.setText(_translate("MainWindow", "Zaman (Yıl):"))
        self.label_6.setText(_translate("MainWindow", "Dev@KivancCoban"))

    # Butonları fonksiyonlara bağlama
        self.basitFaizBtn.clicked.connect(self.basitFaizHesapla)
        self.bilesikFaizBtn.clicked.connect(self.bilesikFaizHesapla)
        self.gelecekDBtn.clicked.connect(self.gelecekDegerHesapla)
        self.bugunkuDBtn.clicked.connect(self.bugunkuDegerHesapla)

    image_path=""
    
    def degiskenleriAl(self):
            try:
                miktar = float(self.paraText.toPlainText())
                faizOran = float(self.faizText.toPlainText())
                zaman = float(self.zamanText.toPlainText())
                taksit_text = float(self.taksitText.toPlainText()) 
                vade = float(self.vadeText.toPlainText()) 
            except ValueError:
            
                return None, None, None, None ,None
            return miktar, faizOran, zaman, vade , taksit_text
    
    def resimYukle(self, image_path):
        try:
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                raise ValueError(f"resim yüklenemedi: {image_path}")
            self.formulLbl.setPixmap(pixmap)
            self.formulLbl.show()
        except Exception as e:
            self.showErrorMessage(f"resim yüklenemedi: {str(e)}")
    
    def basitFaizHesapla(self):
        miktar, faizOran, zaman, _, _ = self.degiskenleriAl()

        if None in (miktar, faizOran, zaman):
            self.showErrorMessage("Takist tutarı hariç diğer değişkenleri giriniz")
            return

        sonuc = round(miktar * (1 + (faizOran / 100) * zaman),2)
        self.sonucText.setText(f"Basit Faiz Sonucu: {sonuc}")
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "basitFaiz.png")
        self.resimYukle(image_path)

    def bilesikFaizHesapla(self):
        miktar, faizOran, zaman, vade,_ = self.degiskenleriAl()

        if None in (miktar, faizOran, zaman, vade):
            return
        
        if vade > 0:
            sonuc = round(miktar * (1 + (faizOran / 100) / float(12 / vade))**(float(12/vade) * zaman),2)
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bilesikFaiz1.png")
        elif vade == 0 :
            sonuc = round((miktar * (1+(faizOran/100)) ** zaman),2)
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bilesikFaiz.png")
        
        else:
            self.showErrorMessage("Hatalı vade giriş")
            return
        self.sonucText.setText(f"Bileşik Faiz sonucu: {sonuc}")
        self.resimYukle(image_path)
        
    def gelecekDegerHesapla(self):
        miktar,faizOran,zaman,vade,taksit_text = self.degiskenleriAl()
        if None in ( faizOran, zaman,taksit_text):
            return
        if (vade ==0 or vade == None) or (miktar==0 or miktar==None):
            sonuc = round(taksit_text*((((1+(faizOran/100))**zaman)-1)/(faizOran/100)),2)
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gelecekDeger.png")
        else:
            sonuc = round(miktar*((faizOran/100)/(((1+(faizOran/100))**vade)-1)),2) 
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gelecekDeger1.png")
        self.sonucText.setText(f"Gelecek Değer anüite Sonucu: {sonuc}")
        self.resimYukle(image_path)

    def bugunkuDegerHesapla(self):
        miktar,faizOran,zaman,_,taksit_text = self.degiskenleriAl()
        if None in (faizOran,zaman,taksit_text):
            return
        if (miktar == 0) or (miktar == None):
            sonuc = round(taksit_text*((((1+(faizOran/100))**zaman)-1)/((faizOran/100)*((1+(faizOran/100))**zaman))),2)
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bugunkuDeger.png")
        else:
            sonuc = round(miktar*((faizOran/100)*((1+(faizOran/100))**zaman)/(((1+(faizOran/100))**zaman)-1)),2)
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bugunkuDeger1.png")
        self.sonucText.setText(f"Bugünkü değer anüite sonucu: {sonuc}")
        
        self.resimYukle(image_path)

    def showErrorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Hata")
        msg_box.setText(message)
        msg_box.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

