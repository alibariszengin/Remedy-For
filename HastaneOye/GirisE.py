import _sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import time


class Pencere(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = _sqlite3.connect("Hastane.db")
        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If not exists Hastalar (Ad TEXT,Soyad TEXT,Tc TEXT,Sigorta TEXT,Parola TEXT)")
        self.cursor.execute("Create Table If not exists Doktorlar (Ad TEXT,Soyad TEXT,Tc TEXT,Parola TEXT,Alanı TEXT)")
        self.baglanti.commit()

    def init_ui(self):
        loadUi("untitled.ui", self)
        self.pushButton_2.setText("Hasta Girişi")
        self.pushButton_1.setText("Doktor Girişi")
        self.pushButton_2.clicked.connect(self.HastaGiris)
        self.pushButton_1.clicked.connect(self.DoktorGiris)

    def HastaGiris(self):

        loadUi("hastagiris.ui", self)
        self.pushButton_1_1.setText("Giris")
        self.pushButton_1_2.setText("Kaydol")

        self.pushButton_1_1.clicked.connect(self.GirisBilgi)
        self.pushButton_1_2.clicked.connect(self.Kayit)
        self.pushButton_bas.clicked.connect(self.init_ui)

    def GirisBilgi(self):
        loadUi("girisbilgi.ui", self)
        self.pushButton_ggeri.clicked.connect(self.HastaGiris)
        self.pushButton_gileri.clicked.connect(self.GirisKontrol)

    def GirisKontrol(self):
        self.Tc_tut = self.lineEdit_tc.text()
        Sifre = self.lineEdit_sifre.text()
        self.cursor.execute("Select * From Hastalar Where Tc = ? and Parola = ?", (self.Tc_tut, Sifre))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.label_hata.setText("Böyle Bir Kullanıcı Yok\nLütfen Tekrar Deneyin")
        else:
            QMessageBox.about(self, "Giriş Durumu", "Giriş Başarılı")
            self.HastaMenu()

    def Kayit(self):
        loadUi("kayit.ui", self)
        self.pushButton_kaydol.clicked.connect(self.Kaydet)
        self.pushButton_kgeri.clicked.connect(self.HastaGiris)

    def Kaydet(self):
        ad = self.lineEdit_kad.text()
        soyad = self.lineEdit_ksoyad.text()
        tc = self.lineEdit_ktc.text()
        sigorta = self.lineEdit_ksigorta.text()
        parola = self.lineEdit_ksifre.text()
        parolaCheck = self.lineEdit_ksifretekrar.text()
        bosKontrol = (ad, soyad, tc, sigorta, parola, parolaCheck)
        a = 0
        for i in bosKontrol:

            if len(i) != 0:
                a = a + 1
            if a != 6:
                self.label_bos.setText("Lütfen Boş Alan Bırakmayınız.")
            else:
                self.label_bos.setText("")
        if (parola != parolaCheck):
            self.label_chec.setText("Parola Değerleri Uyuşmuyor.")
            self.label_check.setText("Tekrar Giriniz.")
        else:
            self.label_chec.setText("")
            self.label_check.setText("")
        if len(tc) != 11:
            self.label_tcwar.setText("Tc Kimlik No 11 Haneli Olmalıdır.")
        else:
            self.label_tcwar.setText("")
            if (parola == parolaCheck and a == 6):
                self.KayitEkle(ad, soyad, tc, sigorta, parola)

    def KayitEkle(self, ad, soyad, tc, sigorta, parola):

        self.cursor.execute("Select * From Hastalar Where Tc = ?", (tc,))
        data = self.cursor.fetchall()
        if len(data) == 0:

            QMessageBox.about(self, "Kayıt", "Kaydınız Başarıyla Eklenmiştir.Giriş Sayfasına Yönlendiriliyorsunuz.")
            self.cursor.execute("Insert into Hastalar Values(?,?,?,?,?)", (ad, soyad, tc, sigorta, parola))
            self.baglanti.commit()
        else:
            QMessageBox.about(self, "Kayıt", "Zaten Kaydınızın Olduğu Gözüküyor.Giriş Sayfasına Yönlendiriliyorsunuz.")
        self.GirisBilgi()
    def HastaMenu(self):
        loadUi("HastaMenu.ui", self)
        self.pushButton_Randevu.clicked.connect(self.Randevucu)
        self.kontrol=0
        #############################################################
        self.pushButton_Muayene.clicked.connect(self.RandevuGecmisi)
        ##############################################################
        self.pushButton_hcikis.clicked.connect(self.Cikis)
    def Randevucu(self):
        loadUi("randevu.ui", self)
        self.a="Seçiniz.."
        self.comboBox.addItem(self.a)
        self.comboBox_2.addItem(self.a)
        self.comboBox_3.addItem(self.a)
        self.pushButton_RaAl.clicked.connect(self.Ranalindi)
        self.ComboAlan()
        
        
    ##############################
    
    def RandevuGecmisi(self):
        loadUi("gecmisrandevu.ui", self)
        if(self.kontrol==0):
            self.pushButton_grgeri.clicked.connect(self.HastaMenu)
        else:
            self.pushButton_grgeri.clicked.connect(self.Hastaisimtc)
        
        Hasta=self.Tc_tut
        self.cursor.execute("Select * From Randevular Where Hasta = ?", (Hasta,))
        data = self.cursor.fetchall()
        
        self.tableWidget.clearContents()
        
        row = self.tableWidget.rowCount()
        
        for x in data:
            self.tableWidget.setRowCount(row + 1)
            
            hafta = x[2][0:3]
            ay = x[2][3:6]
            gun = x[2][6:8]
            yil = x[2][8:12]
            
            tarih = gun + "/" + ay + "/" + yil + " (" + hafta + ")"
            
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(tarih))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(x[3]))
            
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(x[1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(x[4]))
            row = row + 1
        


    ################################    
        

    def ComboAlan(self):
        self.Alan()
        self.comboBox.currentIndexChanged.connect(self.ComboDoktor)

    def ComboDoktor(self):
        self.comboBox_2.setEnabled(True)

        self.DokSec()
        self.comboBox_2.currentIndexChanged.connect(self.randevuKontrol)




        #self.randevuKontrol()

        #self.comboBox.currentIndexChanged.connect(self.DokSec)
        ####################################################################################################
        #self.comboBox_2.currentIndexChanged.connect(self.randevuKontrol)
        #self.calendarWidget.clicked.connect(self.randevuKontrol)
        ###################################################################################################
        #self.pushButton_RaAl.clicked.connect(self.RanAlındı)
    def Ranalindi(self):

        if self.comboBox.currentText() == 'Seçiniz..' or self.comboBox_2.currentText() == 'Seçiniz..' or self.comboBox_3.currentText() == 'Seçiniz..':
            QMessageBox.about(self, "Randevu", "Randevunuz alınamadı")
        else:
            self.OdAlan = self.comboBox.currentText()
            self.OdDoktor = self.comboBox_2.currentText()
            self.OdSaat = self.comboBox_3.currentText()
            self.OdDate = self.calendarWidget.selectedDate().toString()
            self.OdDate = self.OdDate.replace(" ", "")


            QMessageBox.about(self, "Randevu", "Randevunuz Isteğiniz Başarıyla Alınmıştır.Ödeme Ekranına Yönlendiriliyorsunuz.")
            self.Odeme()


    def Odeme(self):
        loadUi("Odemesay.ui", self)
        self.pushButton_ode.clicked.connect(self.OdemeBasarili)
        self.pushButton_ogeri.clicked.connect(self.Randevucu)
    def OdemeBasarili(self):
        ad = self.lineEdit_kad.text()
        soyad = self.lineEdit_ksoyad.text()
        tc = self.lineEdit_ktc.text()
        sigorta = self.lineEdit_ksigorta.text()
        parola = self.lineEdit_ksifre.text()

        bosKontrol = (ad, soyad, tc, sigorta, parola)
        a = 0
        for i in bosKontrol:

            if len(i) != 0:
                a = a + 1
            if a != 5:
                self.label_bos.setText("Lütfen Boş Alan Bırakmayınız.")
            else:
                self.label_bos.setText("")
                Hasta = self.Tc_tut

                self.cursor.execute("Insert into Randevular Values(?,?,?,?,?)", (Hasta, self.OdDoktor, self.OdDate, self.OdSaat, self.OdAlan))
                self.baglanti.commit()
                QMessageBox.question(self, "Odeme Başarılı","Randevunuz kaydedildi.Ödemeniz sigortanızdan kesildi,kalan kısım kartınzıdan çekildi.Makbuz Almak İster misiniz?",)
                self.close()

    def Alan(self):


        self.cursor.execute("Select * From Doktorlar")
        data = self.cursor.fetchall()

        for row in data:
            if (self.comboBox.findText(row[4]) == -1):
                self.comboBox.addItem(row[4])

        #self.comboBox.currentIndexChanged.connect(self.Doksec)
        #self.pushButton_bolum.clicked.connect(self.DokSec)
    def DokSec(self):
        self.comboBox_2.clear()
        self.bolum = self.comboBox.currentText()
        self.cursor.execute("Select * From Doktorlar Where Alanı=?",(self.bolum,))
        data = self.cursor.fetchall()
        self.comboBox_2.addItem(self.a)
        for row in data:
            if self.comboBox_2.findText(row[0]) == -1:
                self.comboBox_2.addItem(row[0]+" "+row[1])

        #self.saatYenile()
        #self.randevuKontrol()

    def saatYenile(self):
        saatler = ["Seçiniz..","09:00","09:15","09:30","09:45","10:00","10:15","10:30","10:45","11:00","11:15","11:30","11:45","13:00","13:15","13:30","13:45","14:00","14:15","14:30","14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45",]

        for saat in saatler:
            if self.comboBox_3.findText(saat) == -1:
                self.comboBox_3.addItem(saat)

    # direk tarihi ve doktoru kontrol eden ve ona gore 3. combobox u ayarlayan fonksiyona gidiyor bunu silip yukarda direk self.randevuKontrol() yazilabilir


    def randevuKontrol(self):

        self.comboBox_3.clear()
        self.comboBox_3.setEnabled(True)
        self.calendarWidget.clicked.connect(self.randevuKontrol)
        self.saatYenile()

        doc = self.comboBox_2.currentText()
        date = self.calendarWidget.selectedDate().toString()
        date = date.replace(" ", "")

        self.cursor.execute("Select * From Randevular Where Doktor = ? and Tarih = ? ",(doc, date))
        data = self.cursor.fetchall()



        if len(data) == 0:
            self.label_Durum.setText("Butun saatler uygun")
            self.label_Durum_2.setText(" ")

            #QMessageBox.about(self,"Durum","Musait hepsi")
        else:

            self.label_Durum.setText("Musait Olan Randevu")
            self.label_Durum_2.setText("Zamanları Bunlardır.")
            for doluSaatler in data:
                index = self.comboBox_3.findText(doluSaatler[3])
                self.comboBox_3.removeItem(index)

        #self.pushButton_RaAl.clicked.connect(self.Ranalindi)

        # QMessageBox fonksiyonlari hata verdi butun saatler doluysa (data boyutu max ise) messagebox ile bu gune randevu alinamaz denebilir
        #Bunu halletim Title kısmını girmediğin için hata vermiş ama durmadan açılıyor o yuzden aşagı yazı koyayaım dedim sen de bakarsun bi.
        #hatta çalışan halini bırakayım

    def DoktorGiris(self):
        loadUi("girisbilgi.ui", self)
        self.pushButton_ggeri.clicked.connect(self.init_ui)
        self.pushButton_gileri.clicked.connect(self.DGirisKontrol)

    def DGirisKontrol(self):
        Tc = self.lineEdit_tc.text()
        Sifre = self.lineEdit_sifre.text()
        self.cursor.execute("Select * From Doktorlar Where Tc = ? and Parola = ?", (Tc, Sifre))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.label_hata.setText("Böyle Bir Doktor Yok\nLütfen Tekrar Deneyin")
        else:
            self.DoktorAdi = data[0][0]
            QMessageBox.about(self, "Giriş Durumu", "Hoşgeldiniz {}.".format(self.DoktorAdi))
            self.DoktorMenu()

    def DoktorMenu(self):
        loadUi("DoktorMenu.ui",self)
        self.pushButton_Muayene.clicked.connect(self.Hastaisimtc)
        self.pushButton_Lab.clicked.connect(self.Lab)
        self.pushButton_Rapor.clicked.connect(self.Raporlama)
        self.pushButton_cikis.clicked.connect(self.Cikis)

    def Cikis(self):
        self.close()
    def Raporlama(self):
        loadUi("raporlamalar.ui",self)
        self.pushButton_rgeri.clicked.connect(self.DoktorMenu)
        self.cursor.execute("Select distinct Doktor From Randevular")
        doktorname = self.cursor.fetchall()

        self.tableWidget_1.clearContents()

        row = self.tableWidget_1.rowCount()



        for i in doktorname:

            self.cursor.execute("SELECT count(*) From Randevular where Doktor=(?) ", (i),)
            sayi=self.cursor.fetchall()
            self.tableWidget_1.setRowCount(row + 1)


            self.tableWidget_1.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))

            sayi=str(sayi)
            if sayi[3]==",":
                sayi=sayi[2:3]
            else:
                sayi=sayi[2:4]
            self.tableWidget_1.setItem(row, 1, QtWidgets.QTableWidgetItem(sayi))

            row = row + 1


    def Lab(self):
        loadUi("labistak.ui", self)
        self.cursor.execute("Create table if not exists Lab(Doktor TEXT , Istek TEXT )")
        self.baglanti.commit()
        self.pushButton_istek.clicked.connect(self.Istek)
        self.pushButton_takip.clicked.connect(self.Takip)
        self.pushButton_labgeri.clicked.connect(self.DoktorMenu)

    def Takip(self):
        QMessageBox.about(self,"Yönlendirme","Merhabalar Doktor {},işlemde olan tahlillerinizin listesi yükleniyor.".format(self.DoktorAdi))
        loadUi("tahlillist.ui", self)

        self.cursor.execute("Select * From Lab Where Doktor = ?", (self.DoktorAdi,))
        data = self.cursor.fetchall()

        self.tableWidget.clearContents()

        row = self.tableWidget.rowCount()

        for x in data:
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(x[1]))
            row = row + 1
        self.pushButton_grgeri.clicked.connect(self.Lab)
    def Istek(self):
        loadUi("tahlil.ui", self)
        self.pushButton_istekgeri.clicked.connect(self.Lab)
        self.pushButton_gonder.clicked.connect(self.IstekGonder)
    def IstekGonder(self):
        if (self.radioButton_kan.isChecked()):
            radio = "Kan Tahlili"
        elif (self.radioButton_idrar.isChecked()):
            radio = "Idrar Tahlili"
        else:
            radio = "Mikroskobik Tahlil"
        self.cursor.execute("Insert into Lab Values(? , ?)",(self.DoktorAdi , radio))

        self.baglanti.commit()
        QMessageBox.about(self,"Tahlil Istek","{} Isteğiniz Kayda Alınmıştır.".format(radio))

    def Hastaisimtc(self):
        loadUi("Sorgu.ui", self)
        self.pushButton_sorgula.clicked.connect(self.Sorgula)
        self.pushButton_sgeri.clicked.connect(self.DoktorMenu)

    def Sorgula(self):
        ad = self.lineEdit_sisim.text()
        soyad = self.lineEdit_ssoyisim.text()
        self.cursor.execute("Select * From Hastalar Where Ad = ? and Soyad = ?", (ad, soyad))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.label_hata.setText("Böyle Bir Hasta Yok\nLütfen Tekrar Deneyin")
            self.lineEdit_sisim.clear()
            self.lineEdit_ssoyisim.clear()
        else:
            self.kontrol=1
            self.Tc_tut = data[0][2]
            self.RandevuGecmisi()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())
