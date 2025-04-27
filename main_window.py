import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QInputDialog, QTextEdit
)
from kutuphane_sistemi import Kitap, Uye, Kutuphane

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.kutuphane = Kutuphane()
        self.setWindowTitle("Kütüphane Yönetim Sistemi")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        btn_kitap_ekle = QPushButton("Kitap Ekle")
        btn_uye_ekle = QPushButton("Üye Ekle")
        btn_odunc_ver = QPushButton("Kitap Ödünç Ver")
        btn_iade_al = QPushButton("Kitap İade Al")
        btn_kitaplari_goster = QPushButton("Kitapları Göster")

        btn_kitap_ekle.clicked.connect(self.kitap_ekle)
        btn_uye_ekle.clicked.connect(self.uye_ekle)
        btn_odunc_ver.clicked.connect(self.kitap_odunc_ver)
        btn_iade_al.clicked.connect(self.kitap_iade_al)
        btn_kitaplari_goster.clicked.connect(self.kitaplari_goster)

        layout.addWidget(btn_kitap_ekle)
        layout.addWidget(btn_uye_ekle)
        layout.addWidget(btn_odunc_ver)
        layout.addWidget(btn_iade_al)
        layout.addWidget(btn_kitaplari_goster)

        self.setLayout(layout)

    def kitap_ekle(self):
        ad, ok1 = QInputDialog.getText(self, "Kitap Adı", "Kitap adı:")
        yazar, ok2 = QInputDialog.getText(self, "Yazar", "Yazar adı:")
        isbn, ok3 = QInputDialog.getText(self, "ISBN", "ISBN numarası:")

        if ok1 and ok2 and ok3:
            yeni_kitap = Kitap(ad, yazar, isbn)
            self.kutuphane.kitap_ekle(yeni_kitap)

    def uye_ekle(self):
        ad, ok1 = QInputDialog.getText(self, "Üye Adı", "Üye adı:")
        uye_id, ok2 = QInputDialog.getText(self, "Üye ID", "Üye ID:")

        if ok1 and ok2:
            yeni_uye = Uye(ad, uye_id)
            self.kutuphane.uye_ekle(yeni_uye)

    def kitap_odunc_ver(self):
        isbn, ok1 = QInputDialog.getText(self, "ISBN", "Kitap ISBN:")
        uye_id, ok2 = QInputDialog.getText(self, "Üye ID", "Üye ID:")

        if ok1 and ok2:
            basarili = self.kutuphane.kitap_odunc_al(isbn, uye_id)
            self.bilgi_mesaji("Başarılı" if basarili else "Kitap ödünç verilemedi.")

    def kitap_iade_al(self):
        isbn, ok = QInputDialog.getText(self, "ISBN", "İade edilecek kitap ISBN:")

        if ok:
            basarili = self.kutuphane.kitap_iade_et(isbn)
            self.bilgi_mesaji("İade alındı" if basarili else "İade edilemedi.")

    def kitaplari_goster(self):
        pencere = QWidget()
        pencere.setWindowTitle("Kayıtlı Kitaplar")
        pencere.setGeometry(150, 150, 400, 300)
        layout = QVBoxLayout()

        kitap_liste = QTextEdit()
        kitap_liste.setReadOnly(True)

        metin = ""
        for kitap in self.kutuphane.kitaplar:
            metin += f"Ad: {kitap.ad}, Yazar: {kitap.yazar}, ISBN: {kitap.isbn}, Durum: {kitap.durum}\n"

        kitap_liste.setText(metin)
        layout.addWidget(kitap_liste)
        pencere.setLayout(layout)
        pencere.show()

        self.kitap_liste_penceresi = pencere

    def bilgi_mesaji(self, mesaj):
        bilgi = QLabel(mesaj)
        pencere = QWidget()
        pencere.setWindowTitle("Bilgi")
        layout = QVBoxLayout()
        layout.addWidget(bilgi)
        pencere.setLayout(layout)
        pencere.setGeometry(200, 200, 200, 100)
        pencere.show()
        self.bilgi_penceresi = pencere

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec_())
