# 🎓 GPA Calculator

Bu proje, üniversite derslerinin notlarını girerek dönemlik ve kümülatif ortalamalarınızı hızlıca hesaplamanızı sağlar. Hiç programlama bilmeyen birisi bile bu projeyi rahatlıkla çalıştırabilir ve kullanabilir.  

---

## 🚀 Nasıl Kurulur?

1. Bilgisayarınızda **Python** kurulu olduğundan emin olun.
2. Projeyi indirdikten sonra **`main.py`** dosyasının bulunduğu klasöre gidin.
3. Terminalde veya komut satırında aşağıdaki komutu çalıştırarak uygulamayı başlatın:

    ```bash
    python main.py
    ```

4. Karşınıza gelecek olan masaüstü arayüzünden (GUI) derslerinizi, **AKTS değerlerinizi** ve **notlarınızı** girerek ortalama hesaplamaya başlayabilirsiniz.

---

## 📂 Proje Yapısı

- **`main.py`** : Uygulamanın başlayacağı ana dosyadır.
- **`__init__.py`** : `gpa_calculator` paketini tanımlar.
- **`ui.py`** : Uygulamanın grafik arayüzünü sağlayan sınıflar burada tanımlıdır (**GPACalculatorApp**).
- **`calculations.py`** : Ders notları üzerinden dönemlik ve kümülatif GPA hesaplamalarını yapan fonksiyonları içerir (**`calculate_cumulative_gpa`**).
- **`data_manager.py`** : **CSV** dosyalarından veri yükleme, kaydetme vb. işlemlerden sorumludur.
- **`default.csv`** : Varsayılan ders ve not verileri bu **CSV** dosyasında bulunur.
- **`LICENSE`** : Projeye ait lisans bilgileri yer alır.

---

## 🎯 Nasıl Kullanılır?

1. Uygulama açıldığında otomatik olarak **`default.csv`** dosyasından varsayılan ders bilgilerini yükler.
2. Derslerin **AKTS değerlerini** ve **notlarını** girin veya düzenleyin.
3. **"CSV Dosyası Yükle"** düğmesine tıklayarak kendi özel dosyanızı yükleyin.
4. **"CSV Olarak Kaydet"** düğmesi ile düzenlediğiniz verileri yeni bir CSV dosyasına kaydedebilirsiniz.
5. Arayüzde görünen **"Dönem Ortalaması"** ve **"Genel Ortalama"** değerleri anında güncellenir.

📌 *Kolay kullanım için sade ve şık bir grafik arayüzü (GUI) sağlanmıştır!*

---

## 📸 Ekran Görüntüsü Örneği

Aşağıdaki uygulamadan bir örnek bulunur:

![Ekran Görüntüsü](/images/screenshot.png)

---

## 🛠 Geliştirme

- Yeni özellikler eklemek veya hataları düzeltmek için **`ui.py`** ve **`calculations.py`** dosyalarındaki kodları inceleyebilirsiniz.
- Kod düzenlemesi yaptıktan sonra, lütfen katkıda bulunma adımlarını izleyin.

---

## 🤝 Katkıda Bulunma

1. Bu projeyi forklayarak kendi hesabınıza kopyalayın.
2. Yeni bir dal (branch) oluşturup değişikliklerinizi yapın.
3. Pull request açarak yaptığınız iyileştirmeleri ve yeni özellikleri paylaşabilirsiniz.

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için **`LICENSE`** dosyasına göz atabilirsiniz.

📚 **Keyifli hesaplamalar!**

