import csv
import tkinter
import os
from tkinter import filedialog
import tkinter.messagebox

def load_data_csv(file_path, default_data_callback):
    """
    CSV dosyasından ders verilerini yükler.

    Args:
        file_path (str): CSV dosyasının yolu.
        default_data_callback (callable): Varsayılan verileri sağlayan fonksiyon.

    Returns:
        list: Dönemlere göre düzenlenmiş ders verileri.
    """
    try:
        ders_data = []
        with open(file_path, "r", encoding="utf-8", newline='') as csvfile:
            print("File being opened:", os.path.abspath(csvfile.name))
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                try:
                    akts_degeri = int(row['akts'])
                except ValueError as ve:
                    print(f"AKTS değeri hatası: {ve}, Satır: {row}")
                    akts_degeri = 0
                semester_name = row['semester']
                course_data = {"code": row['code'], "name": row['name'], "akts": akts_degeri, "grade": row['grade']}
                semester_found = False
                for semester in ders_data:
                    if semester['semester'] == semester_name:
                        semester['courses'].append(course_data)
                        semester_found = True
                        break
                if not semester_found:
                    ders_data.append({"semester": semester_name, "courses": [course_data]})
        print("Veriler CSV dosyasından başarıyla yüklendi.")
        return ders_data
    except FileNotFoundError:
        print("CSV veri dosyası bulunamadı, varsayılan veriler yükleniyor.")
        return default_data_callback()
    except csv.Error as csv_e:
        print(f"CSV okuma hatası: {csv_e}")
        tkinter.messagebox.showerror("Hata", f"CSV dosyası okunurken hata oluştu: {csv_e}")
        return default_data_callback()
    except Exception as e:
        print(f"CSV veri dosyası okunurken genel hata oluştu: {e}")
        tkinter.messagebox.showerror("Hata", f"CSV dosyası yüklenirken genel hata oluştu: {e}")
        return default_data_callback()

def save_data_csv(file_path, semesters_data):
    """
    Ders verilerini CSV dosyasına kaydeder.

    Args:
        file_path (str): CSV dosyasının kaydedileceği yol.
        semesters_data (list): Kaydedilecek dönem bilgileri.
    """
    try:
        with open(file_path, "w", encoding="utf-8", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["semester", "code", "name", "akts", "grade"])
            for semester_data in semesters_data:
                for course in semester_data["courses"]:
                    csv_writer.writerow([
                        semester_data["semester"],
                        course["code"],
                        course["name"],
                        course["akts"],
                        course["grade"]
                    ])
        print(f"Veriler başarıyla CSV dosyasına kaydedildi: {file_path}")
        tkinter.messagebox.showinfo("Başarılı", f"Veriler başarıyla kaydedildi: {file_path}")

    except IOError:
        tkinter.messagebox.showerror("Hata", "CSV veri dosyası yazılırken hata oluştu.")
        print("CSV veri dosyası yazılırken hata oluştu.")

def get_courses_data():
    """
    Varsayılan ders verilerini oluşturur.

    Returns:
        list: Varsayılan ders verileri.
    """
    return [{"semester": f"{i+1}. Sınıf Güz", "courses": []} for i in range(4)]

def ask_save_csv(semesters_data):
    """
    CSV dosyasını kaydetmek için dosya seçme diyalogu açar.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        save_data_csv(file_path, semesters_data)

def ask_open_csv(default_data_callback):
    """
    CSV dosyası yüklemek için dosya seçme diyalogu açar.

    Returns:
        str: Seçilen dosya yolu.
    """
    return filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
