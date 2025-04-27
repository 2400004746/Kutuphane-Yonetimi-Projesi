# Kütüphane Yönetimi Uygulaması - Kullanım Kılavuzu

Bu kılavuz, Kütüphane Yönetimi Uygulaması'nın kullanım adımlarını ve temel işlevlerini açıklar.

---

## Başlangıç

1. Proje dosyalarını bilgisayarınıza indirin.
2. Bilgisayarınızda **Python 3** ve **PyQt5** yüklü olduğundan emin olun.
   - Eğer kurulu değilse şu komutu kullanabilirsiniz:
     ```bash
     pip install PyQt5
     ```
3. Ana uygulamayı başlatmak için terminal/komut satırından şu dosyayı çalıştırın:
   ```bash
   python main_window.py
   ```

---

## Ana İşlevler

### Kitapları Görüntüleme
- Uygulama açıldığında mevcut kitaplar listelenir.
- Kitaplar, `kitaplar.json` dosyasındaki verilere göre yüklenir.

### Kitap Ekleme
1. "Yeni Kitap Ekle" butonuna tıklayın.
2. Kitabın adını, yazarını ve yılını girin.
3. "Ekle" butonuna basarak kitabı kaydedin.
4. Eklenen kitap otomatik olarak listeye ve `kitaplar.json` dosyasına kaydedilir.

### Kitap Arama
- İlgilendiğiniz kitabın adını yazarak hızlıca arama yapabilirsiniz.

### Kitap Silme
1. Listeden bir kitap seçin.
2. "Sil" butonuna tıklayın.
3. Seçilen kitap hem listeden hem de `kitaplar.json` dosyasından silinir.

---

## Dosyalar Hakkında

- **kitaplar.json**:  
  Tüm kayıtlı kitap bilgileri burada saklanır. Kitap ekleme ve silme işlemleri bu dosyada güncelleme yapar.

- **kutuphane_sistemi.py**:  
  Kitap ekleme, silme, listeleme gibi temel işlevleri yöneten Python kodları.

- **main_window.py**:  
  PyQt5 ile oluşturulmuş ana arayüz. Uygulamanın giriş noktasıdır.

- **Kullanım Klavvuzu.txt**:  
  (Bu belge) Uygulamanın nasıl kullanılacağını anlatır.

---

## Sıkça Sorulan Sorular (SSS)

> ❓ Kitaplarımı kaybettim, neden?  
> Eğer `kitaplar.json` dosyası yanlışlıkla silinirse, kayıtlı kitaplar da kaybolur. Düzenli olarak yedek almanız tavsiye edilir.

> ❓ Kitap ekleyemiyorum, ne yapmalıyım?  
> Gerekli tüm alanların (ad, yazar, yıl) doldurulduğundan emin olun.

> ❓ Uygulama açılmıyor, çözüm?  
> Python ve PyQt5'in doğru kurulduğundan emin olun. Terminalde oluşan hata mesajlarını dikkatlice inceleyin.
