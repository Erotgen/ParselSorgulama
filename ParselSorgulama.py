from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pyodbc
import pathlib
from HissedarEkrani import Ui_SecondWindow

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 819)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.ad = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ad.setFont(font)
        self.ad.setObjectName("ad")
        self.gridLayout.addWidget(self.ad, 1, 2, 1, 1)
        self.soyad = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.soyad.setFont(font)
        self.soyad.setObjectName("soyad")
        self.gridLayout.addWidget(self.soyad, 2, 2, 1, 1)
        self.babaad = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.babaad.setFont(font)
        self.babaad.setObjectName("babaad")
        self.gridLayout.addWidget(self.babaad, 3, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.parsel = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parsel.setFont(font)
        self.parsel.setObjectName("parsel")
        self.gridLayout_2.addWidget(self.parsel, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.mahalle = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mahalle.setFont(font)
        self.mahalle.setObjectName("mahalle")
        self.gridLayout_2.addWidget(self.mahalle, 1, 1, 1, 1)
        self.ilce = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ilce.setFont(font)
        self.ilce.setObjectName("ilce")
        self.gridLayout_2.addWidget(self.ilce, 0, 1, 1, 1)
        self.ada = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ada.setFont(font)
        self.ada.setObjectName("ada")
        self.gridLayout_2.addWidget(self.ada, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)
        self.sorgula = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sorgula.setFont(font)
        self.sorgula.setObjectName("sorgula")
        self.sorgula.clicked.connect(self.Output)
        self.gridLayout_4.addWidget(self.sorgula, 0, 1, 1, 1)
        self.temizle = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temizle.setFont(font)
        self.temizle.setObjectName("temizle")
        self.temizle.clicked.connect(self.Clean)
        self.gridLayout_4.addWidget(self.temizle, 1, 0, 1, 1)
        self.klasortemizle = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.klasortemizle.setFont(font)
        self.klasortemizle.setObjectName("klasortemizle")
        self.klasortemizle.clicked.connect(self.CleanFolder)
        self.gridLayout_4.addWidget(self.klasortemizle, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.doubleClicked.connect(self.ShowShareHolder)
        self.tableWidget.setColumnCount(24)
        self.tableWidget.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setEnabled(True)
        self.tableWidget.setSortingEnabled(1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setSizeIncrement(QtCore.QSize(1000, 1000))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        path = pathlib.Path(__file__).parent.resolve()
        folderlist = os.listdir(str(path)+"//Veri Tabanları")
            
        for i in folderlist:
            self.comboBox.addItem(i)
        
        self.comboBox.addItem("Tümü")
        self.comboBox.setCurrentText("Tümü")
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Parsel Sorgulama Programı"))
        self.label.setText(_translate("Form", "Ad:"))
        self.label_2.setText(_translate("Form", "Soyad:"))
        self.label_3.setText(_translate("Form", "Baba Adı:"))
        self.label_6.setText(_translate("Form", "Ada:"))
        self.label_7.setText(_translate("Form", "Parsel:"))
        self.label_4.setText(_translate("Form", "İlçe:"))
        self.label_5.setText(_translate("Form", "Mahalle:"))
        self.sorgula.setText(_translate("Form", "Sorgula"))
        self.temizle.setText(_translate("Form", "Temizle"))
        self.klasortemizle.setText(_translate("Form", "Klasör Temizle"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Adi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Soyadi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "BabaAdi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "TCKimlikNo"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "HissePay"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "HissePayda"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "EdinmeSebebi"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Tarih"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Yevmiye"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Il"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Ilce"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "MahalleKoyAdi"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "Ada"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "Parsel"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "PaftaNo"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "Mevkii"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Form", "Yuzolcum"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Form", "Cilt"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Form", "Sayfa"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Form", "AnaTasinmazNitelik"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("Form", "ArsaPay"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("Form", "ArsaPayda"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("Form", "BagimsizBolumNitelik"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("Form", "ID"))
    
    def Clean(self):
        self.ad.clear()
        self.soyad.clear()
        self.babaad.clear()
        self.ilce.clear()
        self.mahalle.clear()
        self.ada.clear()
        self.parsel.clear()
        self.tableWidget.setRowCount(0)
        self.textBrowser.clear()
    
    def CleanFolder(self):
            
            content = self.comboBox.currentText()
            
            if content == "Tümü":
                path = str(pathlib.Path(__file__).parent.resolve())+"//Veri Tabanları"
                folderlist = os.listdir(path)
                for i in folderlist:
                    path = str(pathlib.Path(__file__).parent.resolve())+"//Veri Tabanları//"+i
                    filelist = os.listdir(path)
                    
                    for p in filelist:
                        if p[-4:] == ".ldb" or p[-4:] == ".LDB" or p[-4:] == ".lDB" or p[-4:] == ".Ldb":
                            os.remove(path+"\\"+p)
                            
            else:
                path = str(pathlib.Path(__file__).parent.resolve())+"//Veri Tabanları//"+content
                file = os.listdir(path)
                
                for i in file:
                    
                    if i[-4:] == ".ldb" or i[-4:] == ".LDB" or i[-4:] == ".lDB" or i[-4:] == ".Ldb":
                        os.remove(path+"\\"+i)
        
    def Change(self, text, decleration):
            
            if decleration == "lower":
                if "İ" in text:
                    text = text.replace("İ","i")
                if "I" in text:
                    text = text.replace("I","ı")  
                if "Ğ" in text:
                    text = text.replace("Ğ","ğ")
                if "Ü" in text:
                    text = text.replace("Ü","ü")
                if "Ö" in text:
                    text = text.replace("Ö","ö")
                if "U" in text:
                    text = text.replace("U","u")
                if "O" in text:
                    text = text.replace("O","o")
                if "Ç" in text:
                    text = text.replace("Ç","ç")
                if "Ş" in text:
                    text = text.replace("Ş","ş")
            
            else:
                if "ı" in text:
                    text = text.replace("ı","I")  
                if "i" in text:
                    text = text.replace("i","İ")
                if "ğ" in text:
                    text = text.replace("ğ","Ğ")
                if "ü" in text:
                    text = text.replace("ü","Ü")
                if "ö" in text:
                    text = text.replace("ö","Ö")
                if "u" in text:
                    text = text.replace("u","U")
                if "o" in text:
                    text = text.replace("o","O")
                if "ç" in text:
                    text = text.replace("ç","Ç")
                if "ş" in text:
                    text = text.replace("ş","Ş")
            
            return text
    
    def ShowShareHolder(self):

        ID = self.tableWidget.item(int(self.tableWidget.currentRow()), 23).text()
        province = self.tableWidget.item(int(self.tableWidget.currentRow()), 9).text()
        district = self.tableWidget.item(int(self.tableWidget.currentRow()), 10).text()
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        self.FindShareHolder(ID, province, district)
    
    def FindShareHolder(self, ID, province, district):
        
        path_database = self.FindDatabase(province, district)

        self.ui.tableWidget2.setRowCount(0)
        self.ui.textBrowser2.clear()
        
        connect = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+path_database+";")
        cursor = connect.cursor()
        
        count_row = 0
        
        execute_pri = cursor.execute("select * from Zemin where ID=?", int(ID))
        data_pri = execute_pri.fetchall()
        
        execute_sec = cursor.execute("select * from ZeminHisse where ZeminRef=?", int(ID))
        data_sec = execute_sec.fetchall()
                    
        for sec in data_sec:
            
            if data_sec == []:

                self.ui.textBrowser2.append(str(ID)+" numaralı taşınmazın üzerinde hissedar bulunamadı.")
                break
            
            rowPosition = self.ui.tableWidget2.rowCount()
            self.ui.tableWidget2.insertRow(rowPosition)
            
            column = 0
            
            listpri = [8, 9, 11, 15, 16, 17, 18, 19, 20, 21, 23, 28, 29, 31]
            listsec = [2, 3, 4, 5, 10, 11, 12, 13, 14]
            
            indexsec = 0
            
            for col_sec in sec:
                
                if indexsec not in listsec:
                    indexsec += 1
                    continue
                
                indexsec += 1
                
                if col_sec == 0:
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                    
                elif type(col_sec) != str and str(col_sec)[-1] == "0" and str(col_sec)[-2] == ".":
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)[0:-2]))
                        
                        
                elif str(col_sec) == "None":
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(" "))            
                        
                    
                elif type(col_sec) != str:
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                        
                else:
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                        
                column += 1      
                
            indexpri = 0
            for col_pri in data_pri[0]:
                
                if indexpri not in listpri:
                    indexpri += 1
                    continue
                
                indexpri += 1
                
                if col_pri == 0:
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
                    
                elif type(col_pri) != str and str(col_pri)[-1] == "0" and str(col_pri)[-2] == ".":
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)[0:-2]))
                        
                    
                elif str(col_pri) == "None":
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(" "))
                        
                    
                elif type(col_pri) != str:
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))

                else:
                    self.ui.tableWidget2.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
                        
                column += 1
                
            count_row += 1
        
        self.ui.textBrowser2.append(str(ID)+" numaralı taşınmazın üzerinde "+str(count_row)+" hissedar bulundu.")
        
    def FindDatabase(self, province, district):
                
        provinceFile = []
        provinceFile_real = []
        districtFile = []
        districtFile_real = []
        
        path1 = str(pathlib.Path(__file__).parent.resolve())+"//Veri Tabanları//"
        provinceFile = os.listdir(path1)
        
        for p in provinceFile:
            if province in p:
                provinceFile_real.append(p)

        path2 = path1+str(provinceFile_real[0])
        districtFile = os.listdir(path2)
        
        text2 = Ui_Form.Change(self, district[1:], "lower")
        text3 = district[0]+text2.lower()
        
        for d in districtFile:
            if text3 in d and d[-4:] == ".MDB":
                districtFile_real.append(d)
        path3 = path2+"//"+str(districtFile_real[0])       
        
        return path3 
        
        
    def ChooseOption(self, option, ilce, mahalle, cursor, pri):
            
            if option == 1:
                execute_sec = cursor.execute("select * from Zemin where ID=?", int(pri[1]))
            
            elif option == 2:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ?", int(pri[1]), "%"+ilce+"%")
            
            elif option == 3:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND MahalleKoyAdi like ?", int(pri[1]), "%"+mahalle+"%")
            
            elif option == 4:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ada like ?", int(pri[1]), "%"+self.ada.text()+"%")
            
            elif option == 5:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Parsel like ?", int(pri[1]), "%"+self.parsel.text()+"%")
            
            elif option == 6:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ? AND MahalleKoyAdi like ?", int(pri[1]), "%"+ilce+"%", "%"+mahalle+"%")
            
            elif option == 7:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ? AND Ada like ?", int(pri[1]), "%"+ilce+"%", "%"+self.ada.text()+"%")
            
            elif option == 8:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ? AND Parsel like ?", int(pri[1]), "%"+ilce+"%", "%"+self.parsel.text()+"%")
            
            elif option == 9:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND MahalleKoyAdi like ? AND Ada like ?", int(pri[1]), "%"+mahalle+"%", "%"+self.ada.text()+"%")
            
            elif option == 10:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND MahalleKoyAdi like ? AND Parsel like ?", int(pri[1]), "%"+mahalle+"%", "%"+self.parsel.text()+"%")
            
            elif option == 11:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ada like ? AND Parsel like ?", int(pri[1]), "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")
            
            elif option == 12:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ? AND MahalleKoyAdi like ? AND Ada like ?", int(pri[1]), "%"+ilce+"%", "%"+mahalle+"%", "%"+self.ada.text()+"%")
            
            elif option == 13:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ? AND MahalleKoyAdi like ? AND Parsel like ?", int(pri[1]), "%"+ilce+"%", "%"+mahalle+"%", "%"+self.parsel.text()+"%")
            
            elif option == 14:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ? AND Ada like ? AND Parsel like ?", int(pri[1]), "%"+ilce+"%", "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")
            
            elif option == 15:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND MahalleKoyAdi like ? AND Ada like ? AND Parsel like ?", int(pri[1]), "%"+mahalle+"%", "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")
            
            elif option == 16:
                execute_sec = cursor.execute("select * from Zemin where ID=? AND Ilce like ? AND MahalleKoyAdi like ? AND Ada like ? AND Parsel like ?", int(pri[1]), "%"+ilce+"%", "%"+mahalle+"%", "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")

            return execute_sec
        
    def RunZeminHisse(self, cursor, count_row ,execute_pri, option, ilce, mahalle):
            
            data_pri = execute_pri.fetchall()
    
            for pri in data_pri:
                execute_sec = self.ChooseOption(1, ilce, mahalle, cursor, pri)
                data_sec = execute_sec.fetchall()
                
                if data_sec == []:

                    data_sec = [(" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                              " ", " ", " ", " ")]
                    if option != 1:
                        continue
 
                else:
                    execute_sec = self.ChooseOption(option, ilce, mahalle, cursor, pri)
                    data_sec = execute_sec.fetchall()
                    
                    if data_sec == []:
                        continue
                
                for sec in data_sec:
                    
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    column = 0 
                    
                    listpri = [2, 3, 4, 5, 10, 11, 12, 13, 14]
                    listsec = [8, 9, 11, 15, 16, 17, 18, 19, 20, 21, 23, 28, 29, 31]
                    
                    indexpri = 0
                    
                    for col_pri in pri:
                        if indexpri not in listpri:
                            indexpri += 1
                            continue
                        
                        indexpri +=1
                        
                        if col_pri == 0:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
                                
                        elif type(col_pri) != str and str(col_pri)[-1] == "0" and str(col_pri)[-2] == ".":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)[0:-2]))
                                
                        elif str(col_pri) == "None":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(" "))
                            
                        elif type(col_pri) != str:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
                            
                        else:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
                        
                        column += 1
                    
                    indexsec = 0

                    for col_sec in sec:
                        if indexsec not in listsec:
                            indexsec += 1
                            continue
                        
                        indexsec +=1
                        
                        if col_sec == 0:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                            
                        elif type(col_sec) != str and str(col_sec)[-1] == "0" and str(col_sec)[-2] == ".":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)[0:-2]))
                            
                        elif str(col_sec) == "None":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(" "))
                            
                        elif type(col_sec) != str:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                            
                        else:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                        
                        column += 1
                        
                    self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(int(sec[0]))))
                        
                    count_row += 1
                
            return count_row

    def RunZemin(self, cursor, count_row, execute_pri):
            
            data_pri = execute_pri.fetchall()
            for pri in data_pri:
                execute_sec = cursor.execute("select * from ZeminHisse where ZeminRef=?", int(pri[0]))
                data_sec = execute_sec.fetchall()
                
                if data_sec == []:

                    data_sec = [(" ", " ", " ", " ", " ", " ", " ", " ", " ")]
      
                for sec in data_sec:
                        
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    column = 0
                    
                    listpri = [8, 9, 11, 15, 16, 17, 18, 19, 20, 21, 23, 28, 29, 31]
                    listsec = [2, 3, 4, 5, 10, 11, 12, 13, 14]
                    
                    indexsec = 0
                    
                    for col_sec in sec:
                        
                        if data_sec != [(" ", " ", " ", " ", " ", " ", " ", " ", " ")]:
                            if indexsec not in listsec:
                                indexsec +=1
                                continue
                            
                            indexsec += 1
                        
                        if col_sec == 0:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                            
                        elif type(col_sec) != str and str(col_sec)[-1] == "0" and str(col_sec)[-2] == ".":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)[0:-2]))
                                
                                
                        elif str(col_sec) == "None":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(" "))            
                                
                            
                        elif type(col_sec) != str:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                                
                        else:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_sec)))
                                
                        column += 1      
                    
                    indexpri = 0
                    for col_pri in pri:
                        
                        if indexpri not in listpri:
                            indexpri += 1
                            continue
                        
                        indexpri += 1
                        
                        if col_pri == 0:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
                            
                        elif type(col_pri) != str and str(col_pri)[-1] == "0" and str(col_pri)[-2] == ".":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)[0:-2]))
                                
                            
                        elif str(col_pri) == "None":
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(" "))
                                
                            
                        elif type(col_pri) != str:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
   
                        else:
                            self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(col_pri)))
                                
                        column += 1
                    
                    self.tableWidget.setItem(count_row, column, QtWidgets.QTableWidgetItem(str(int(pri[0]))))   
                   
                    count_row += 1
                
            return count_row
                    
        
    def Option(self):
            if  self.ilce.text() == "" and self.mahalle.text() == "" and self.ada.text() == "" and self.parsel.text() == "":
                option = 1
                
            elif self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() == "" and self.parsel.text() == "":
                option = 2
            
            elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() == "":
                option = 3
            
            elif self.ilce.text() == "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() == "":
                option = 4
            
            elif self.ilce.text() == "" and self.mahalle.text() == "" and self.ada.text() == "" and self.parsel.text() != "":
                option = 5
            
            elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() == "":
                option = 6
            
            elif self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() == "":
                option = 7
            
            elif self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() == "" and self.parsel.text() != "":
                option = 8
            
            elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() == "":
                option = 9
                
            elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() != "":
                option = 10
            
            elif self.ilce.text() == "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() != "":
                option = 11
            
            elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() == "":
                option = 12
            
            elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() != "":
                option = 13
            
            elif self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() != "":
                option = 14
            
            elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() != "":
                option = 15
            
            elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() != "":
                option = 16
            
            return option
    
    def Result(self, file1, path, content, count_row):
        file = []
        option = self.Option()
        
        ad = self.Change(self.ad.text(), "upper")
        soyad = self.Change(self.soyad.text(), "upper")
        babaad = self.Change(self.babaad.text(), "upper")
        ilce = self.Change(self.ilce.text(), "upper")
        mahalle = self.Change(self.mahalle.text(), "upper")

        
        for check in file1:
            
            if check[-4:] != ".MDB":
                continue
            
            else:
                file.append(check)
        
        if self.ilce.text() != "":
            
            file2 = file
            file = []
            
            text = self.Change(self.ilce.text(), "lower")
            
            for name in file2:
                
                word_real = self.Change(name, "lower")
                if text.lower() in word_real.lower():
                    file.append(name)
                
        for database in file:
            connect = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+path+"\\"+database+";")
            cursor = connect.cursor()
            if self.ad.text() != "" or self.soyad.text() != "" or self.babaad.text() != "":
               
                if self.ad.text() != "" and self.soyad.text() == "" and self.babaad.text() == "":
                    execute_pri = cursor.execute("select * from ZeminHisse where Adi like ?", "%"+ad+"%")
                    count_row = self.RunZeminHisse(cursor, count_row, execute_pri, option, ilce, mahalle)
                
                elif self.ad.text() == "" and self.soyad.text() != "" and self.babaad.text() == "":
                    execute_pri = cursor.execute("select * from ZeminHisse where Soyadi like ?", "%"+soyad+"%")
                    count_row = self.RunZeminHisse(cursor, count_row, execute_pri, option, ilce, mahalle)
                    
                elif self.ad.text() == "" and self.soyad.text() == "" and self.babaad.text() != "":
                    execute_pri = cursor.execute("select * from ZeminHisse where BabaAdi like ?", "%"+babaad+"%")
                    count_row = self.RunZeminHisse(cursor, count_row, execute_pri, option, ilce, mahalle)
                    
                elif self.ad.text() != "" and self.soyad.text() != "" and self.babaad.text() == "":
                    execute_pri = cursor.execute("select * from ZeminHisse where Adi like ? AND Soyadi like ?", "%"+ad+"%", "%"+soyad+"%")
                    count_row = self.RunZeminHisse(cursor, count_row, execute_pri, option, ilce, mahalle)
                    
                elif self.ad.text() != "" and self.soyad.text() == "" and self.babaad.text() != "":
                    execute_pri = cursor.execute("select * from ZeminHisse where Adi like ? AND BabaAdi like ?", "%"+ad+"%", "%"+babaad+"%")
                    count_row = self.RunZeminHisse(cursor, count_row, execute_pri, option, ilce, mahalle)
                    
                elif self.ad.text() == "" and self.soyad.text() != "" and self.babaad.text() != "":
                    execute_pri = cursor.execute("select * from ZeminHisse where Soyadi like ? AND BabaAdi like ?", "%"+soyad+"%", "%"+babaad+"%")
                    count_row = self.RunZeminHisse(cursor, count_row, execute_pri, option, ilce, mahalle)
                    
                elif self.ad.text() != "" and self.soyad.text() != "" and self.babaad.text() != "":
                    execute_pri = cursor.execute("select * from ZeminHisse where Adi like ? AND Soyadi like ? AND BabaAdi like ?", "%"+ad+"%", "%"+soyad+"%", "%"+babaad+"%")
                    count_row = self.RunZeminHisse(cursor, count_row, execute_pri, option, ilce, mahalle)
                    
                self.textBrowser.append(content+" klasöründeki "+database+" veritabanında sorgulama tamamlandı.")

            elif self.ilce.text() != "" or self.mahalle.text() != "" or self.ada.text() != "" or self.parsel.text() != "":
               
                #1
                if self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() == "" and self.parsel.text() == "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ?", "%"+ilce+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)             
                
                #2
                elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() == "":
                    execute_pri = cursor.execute("select * from Zemin where MahalleKoyAdi like ?", "%"+mahalle+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #3
                elif self.ilce.text() == "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() == "":
                    execute_pri = cursor.execute("select * from Zemin where Ada like ?", "%"+self.ada.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #4    
                elif self.ilce.text() == "" and self.mahalle.text() == "" and self.ada.text() == "" and self.parsel.text() != "":
                    execute_pri = cursor.execute("select * from Zemin where Parsel like ?", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #5
                elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() == "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ? AND MahalleKoyAdi like ?", "%"+ilce+"%", "%"+mahalle+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #6
                elif self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() == "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ? AND Ada like ?", "%"+ilce+"%", "%"+self.ada.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #7
                elif self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() == "" and self.parsel.text() != "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ? AND Parsel like ?", "%"+ilce+"%", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #8
                elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() == "":
                    execute_pri = cursor.execute("select * from Zemin where MahalleKoyAdi like ? AND Ada like ?", "%"+mahalle+"%", "%"+self.ada.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #9
                elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() != "":
                    execute_pri = cursor.execute("select * from Zemin where MahalleKoyAdi like ? AND Parsel like?", "%"+mahalle+"%", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #10
                elif self.ilce.text() == "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() != "":
                    
                    execute_pri = cursor.execute("select * from Zemin where Ada like ? AND Parsel like ?", "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #11
                elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() == "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ? AND MahalleKoyAdi like ? AND Ada like ?", "%"+ilce+"%", "%"+mahalle+"%", "%"+self.ada.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #12
                elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() == "" and self.parsel.text() != "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ? AND MahalleKoyAdi like ? AND Parsel like ?", "%"+ilce+"%", "%"+mahalle+"%", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #13
                elif self.ilce.text() != "" and self.mahalle.text() == "" and self.ada.text() != "" and self.parsel.text() != "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ? AND Ada like ? AND Parsel like ?", "%"+ilce+"%", "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #14
                elif self.ilce.text() == "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() != "":
                    execute_pri = cursor.execute("select * from Zemin where MahalleKoyAdi like ? AND Ada like ? AND Parsel like ?", "%"+mahalle+"%", "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                
                #15
                elif self.ilce.text() != "" and self.mahalle.text() != "" and self.ada.text() != "" and self.parsel.text() != "":
                    execute_pri = cursor.execute("select * from Zemin where Ilce like ? AND MahalleKoyAdi like ? AND Ada like ? AND Parsel like ?", "%"+ilce+"%", "%"+mahalle+"%", "%"+self.ada.text()+"%", "%"+self.parsel.text()+"%")
                    count_row = self.RunZemin(cursor, count_row, execute_pri)
                    
                self.textBrowser.append(content+" klasöründeki "+database+" veritabanında sorgulama tamamlandı.")
                
        return count_row
        
    def Output(self):
            
            self.tableWidget.setRowCount(0)
            self.textBrowser.clear()
        
            content = self.comboBox.currentText()
            count_row = 0
            if content == "Tümü":
                path = str(pathlib.Path(__file__).parent.resolve())+"//Veri Tabanları"
                folders = os.listdir(path)
            
                for i in folders:
                    path = str(pathlib.Path(__file__).parent.resolve())+"//Veri Tabanları//"+i
                    file1 = os.listdir(path)
                    if file1 == []:
                        continue
                    
                    if self.ilce.text() != "":
                        
                        file2 = file1
                        
                        text = self.Change(self.ilce.text(), "lower")
                        file3 = []
                        for name in file2:
                            
                            word_real = self.Change(name, "lower")
                            if text.lower() in word_real.lower():
                                file3.append(name)
                        
                        if file3 == []:
                            continue

                    result = self.Result(file1, path, i, count_row)
                    count_row = result
            else:
                path = str(pathlib.Path(__file__).parent.resolve())+"//Veri Tabanları//"+content
                file1 = os.listdir(path)
                self.Result(file1, path, content, count_row)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
    
