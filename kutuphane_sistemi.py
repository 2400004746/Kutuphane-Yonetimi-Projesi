import json
import os

class Kitap:
    def __init__(self, ad, yazar, isbn):
        self.ad = ad
        self.yazar = yazar
        self.isbn = isbn
        self.durum = "Mevcut"

class Uye:
    def __init__(self, ad, uye_id):
        self.ad = ad
        self.uye_id = uye_id

class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.uyeler = []
        self.odunc_kitaplar = {}
        self.kitap_dosyasi = "kitaplar.json"
        self.kitaplari_yukle()

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        self.kitaplari_kaydet()

    def uye_ekle(self, uye):
        self.uyeler.append(uye)

    def kitap_odunc_al(self, isbn, uye_id):
        for kitap in self.kitaplar:
            if kitap.isbn == isbn and kitap.durum == "Mevcut":
                kitap.durum = "Ödünç"
                self.odunc_kitaplar[isbn] = uye_id
                self.kitaplari_kaydet()
                return True
        return False

    def kitap_iade_et(self, isbn):
        for kitap in self.kitaplar:
            if kitap.isbn == isbn and kitap.durum == "Ödünç":
                kitap.durum = "Mevcut"
                del self.odunc_kitaplar[isbn]
                self.kitaplari_kaydet()
                return True
        return False

    def kitaplari_kaydet(self):
        kitaplar_json = [
            {"ad": k.ad, "yazar": k.yazar, "isbn": k.isbn, "durum": k.durum}
            for k in self.kitaplar
        ]
        with open(self.kitap_dosyasi, "w", encoding="utf-8") as f:
            json.dump(kitaplar_json, f, ensure_ascii=False, indent=4)

    def kitaplari_yukle(self):
        if os.path.exists(self.kitap_dosyasi):
            with open(self.kitap_dosyasi, "r", encoding="utf-8") as f:
                kitaplar_json = json.load(f)
                for k in kitaplar_json:
                    kitap = Kitap(k["ad"], k["yazar"], k["isbn"])
                    kitap.durum = k["durum"]
                    self.kitaplar.append(kitap)
