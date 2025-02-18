# 🎓 GPA Calculator

Bu proje, üniversite derslerinin notlarını girerek dönemlik ve kümülatif ortalamalarınızı hızlıca hesaplamanızı sağlar. Hiç programlama bilmeyen birisi bile bu projeyi rahatlıkla çalıştırabilir ve kullanabilir.  

---

## 🚀 Uygulamayı `.exe` Dosyasıyla Kullanma (En Basit Yöntem!)

Bu uygulamayı Python veya herhangi başka bir kurulum gerekmeden kolayca kullanmak için:

1. GitHub **Releases** sekmesine gidin ve en güncel sürümün zip dosyasını (örnek: `gpa_calculator_v1.x.x.zip`) indirin.
2. İndirdiğiniz zip arşivini açın. İçerisinde iki dosya bulacaksınız:  
   - **`main.exe`**  
   - **`default.csv`**  
3. Bu iki dosyayı mutlaka **aynı klasör** içinde tutun. (Örneğin masaüstüne bir `GPA-Calculator` klasörü oluşturup ikisini oraya kopyalayın.)
4. **`main.exe`** dosyasını çalıştırın (çift tıklayın).  
5. Uygulamada listelenen derslerinizi düzenleyebilir, yeni notlar girebilir veya verilerinizi CSV olarak kaydedebilirsiniz.

> Eğer uygulama `default.csv` dosyasını göremezse, hatalı veya eksik veri yüklenebilir. Bu yüzden `main.exe` ile `default.csv` dosyasının aynı dizinde olduğundan emin olun.

Not: Bu adımda hata alıyorsanız bir sonraki adımı da uygulayabilirsiniz.

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
3. **"CSV Olarak Kaydet"** düğmesi ile her senaryonuzu yeni bir CSV dosyasına kaydedebilirsiniz.
4. **"CSV Dosyası Yükle"** düğmesine tıklayarak daha önceden kaydettiğiniz çeşitli senaryolardan birini yükleyin.
5. Arayüzde görünen **"Dönem Ortalaması"** ve **"Genel Ortalama"** değerleri anında güncellenir.

📌 *Kolay kullanım için sade ve şık bir grafik arayüzü (GUI) sağlanmıştır!*

---

## 📝 Ders Listesini Düzenleme

Varsayılan ders listesini kendi ihtiyaçlarınıza göre düzenlemek için:

1. **`default.csv`** dosyasını herhangi bir metin editörü (Not Defteri, VS Code vb.) veya Excel ile açın.
2. CSV dosyasının formatı aşağıdaki gibidir:
   ```csv
   semester,code,name,akts,grade
   1. Sınıf Güz,MAT101,Matematik I,6,
   ```
   Her satır bir dersi temsil eder ve virgüllerle ayrılmış 5 alan içerir:
   - **semester**: Dönem adı (örn: "1. Sınıf Güz", "2. Sınıf Bahar")
   - **code**: Ders kodu (örn: "MAT101", "FIZ102")
   - **name**: Dersin tam adı
   - **akts**: Dersin AKTS değeri
   - **grade**: Harf notu (boş bırakılabilir)

3. **Yeni Ders Eklemek İçin:**
   - Yeni bir satır ekleyin
   - Yukarıdaki formata uygun şekilde dersin bilgilerini girin
   - Harf notunu başlangıçta boş bırakabilirsiniz

4. **Ders Silmek İçin:**
   - Silmek istediğiniz dersin satırını tamamen silin

5. **Önemli Notlar:**
   - Virgülleri ve sütun sırasını bozmamaya dikkat edin
   - Dosyanın ilk satırını (`semester,code,name,akts,grade`) silmeyin
   - Her dersin AKTS değerini sayı olarak girin
   - Dönem adlarını tutarlı bir şekilde yazın (örn: hep "1. Sınıf Güz" formatında)

6. **Değişiklikleri Kaydetme:**
   - Düzenlemeleri bitirdikten sonra dosyayı kaydedin
   - Dosya formatının "CSV" olarak kaldığından emin olun
   - Uygulamayı yeniden başlattığınızda yeni ders listeniz yüklenecektir

> 💡 **İpucu**: Yaptığınız değişikliklerden memnun kalmazsanız, GitHub'dan orijinal `default.csv` dosyasını tekrar indirebilirsiniz.

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

