import tkinter
import customtkinter
import tkinter.messagebox
from gpa_calculator.data_manager import (
    load_data_csv, save_data_csv, get_courses_data,
    ask_save_csv, ask_open_csv
)
from gpa_calculator.calculations import (
    calculate_semester_gpa, calculate_cumulative_gpa
)
class RemoveCourseDialog(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ders Sil")
        self.geometry("500x400")

        # Dialog penceresini en öne getir
        self.lift()  # Pencereyi öne getirir
        self.focus_force()  # Klavye odağını zorla bu pencereye verir
        self.grab_set()  # Modal pencere yapar (ana pencereyle etkileşimi engeller)
        
        # Başlık
        self.title_label = customtkinter.CTkLabel(
            self, 
            text="Silmek İstediğiniz Dersi Seçin:",
            font=customtkinter.CTkFont(size=16, weight="bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Ders listesi için scrollable frame
        self.course_frame = customtkinter.CTkScrollableFrame(self)
        self.course_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Dersleri listele
        self.course_buttons = []
        for sem_data in parent.semesters_data:
            # Dönem başlığı
            semester_label = customtkinter.CTkLabel(
                self.course_frame,
                text=sem_data['semester'],
                font=customtkinter.CTkFont(weight="bold")
            )
            semester_label.pack(pady=(10,5), anchor="w")
            
            # Dönemdeki dersler
            for course in sem_data['courses']:
                course_text = f"{course['code']} - {course['name']} ({course['akts']} AKTS)"
                course_button = customtkinter.CTkButton(
                    self.course_frame,
                    text=course_text,
                    command=lambda s=sem_data['semester'], c=course['code']: self.delete_course(s, c)
                )
                course_button.pack(pady=2, fill="x")
                self.course_buttons.append(course_button)
        
        self.parent = parent
    
    def delete_course(self, semester, code):
        if tkinter.messagebox.askyesno("Onay", "Bu dersi silmek istediğinizden emin misiniz?"):
            self.parent.remove_course(semester, code)
            self.parent.calculate_all_gpa()  # Ana penceredeki hesaplamaları güncelle
            self.destroy()



class AddCourseDialog(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Yeni Ders Ekle")
        self.geometry("400x300")
        
        # Dialog penceresini en öne getir
        self.lift()  # Pencereyi öne getirir
        self.focus_force()  # Klavye odağını zorla bu pencereye verir
        self.grab_set()  # Modal pencere yapar (ana pencereyle etkileşimi engeller)
        
        # Dönem seçimi
        self.semester_label = customtkinter.CTkLabel(self, text="Dönem:")
        self.semester_label.grid(row=0, column=0, padx=10, pady=5)
        
        # Dönem seçimi
        self.semester_var = customtkinter.StringVar()
        self.semester_combo = customtkinter.CTkComboBox(
            self,
            values=[
                "1. Sınıf Güz", 
                "1. Sınıf Bahar", 
                "2. Sınıf Güz", 
                "2. Sınıf Bahar",
                "3. Sınıf Güz",
                "3. Sınıf Bahar",
                "4. Sınıf Güz",
                "4. Sınıf Bahar"
            ],
            variable=self.semester_var
        )
        self.semester_combo.grid(row=0, column=1, padx=10, pady=5)
        
        # Ders kodu girişi
        self.code_label = customtkinter.CTkLabel(self, text="Ders Kodu:")
        self.code_label.grid(row=1, column=0, padx=10, pady=5)
        self.code_entry = customtkinter.CTkEntry(self, placeholder_text="Ders Kodu")
        self.code_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Ders adı girişi
        self.name_label = customtkinter.CTkLabel(self, text="Ders Adı:")
        self.name_label.grid(row=2, column=0, padx=10, pady=5)
        self.name_entry = customtkinter.CTkEntry(self, placeholder_text="Ders Adı")
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # AKTS girişi
        self.akts_label = customtkinter.CTkLabel(self, text="AKTS:")
        self.akts_label.grid(row=3, column=0, padx=10, pady=5)
        self.akts_entry = customtkinter.CTkEntry(self, placeholder_text="AKTS")
        self.akts_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Kaydet butonu
        self.save_button = customtkinter.CTkButton(
            self,
            text="Kaydet",
            command=self.save_course
        )
        self.save_button.grid(row=4, column=0, columnspan=2, pady=20)
        
        self.parent = parent
        
    def save_course(self):
        try:
            semester = self.semester_var.get()
            code = self.code_entry.get()
            name = self.name_entry.get()
            akts = int(self.akts_entry.get())
            
            if not all([semester, code, name, akts]):
                tkinter.messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")
                return
                
            self.parent.add_course(semester, code, name, akts)
            self.destroy()
            
        except ValueError:
            tkinter.messagebox.showerror("Hata", "AKTS değeri sayı olmalıdır!")

class GPACalculatorApp(customtkinter.CTk):
    """
    GPA Hesaplama Uygulaması
    """
    def __init__(self):
        """
        Uygulama başlatıldığında çalışacak fonksiyon.
        """
        super().__init__()
        self.current_file = "default.csv"  # Mevcut dosya yolunu tut
        self.semesters_data = load_data_csv(self.current_file, get_courses_data)

        self.title("GPA Hesaplama Uygulaması")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grade_points = {
            "AA": 4.0, "BA": 3.5, "BB": 3.0, "CB": 2.5, "CC": 2.0,
            "DC": 1.5, "DD": 1.0, "FF": 0.0, "": ""
        }
        self.grade_options = list(self.grade_points.keys())
        self.grade_options.remove("")
        self.grade_options.insert(0, "")

        self.semester_frames = []
        self.semester_gpa_labels = []
        self.semester_akts_labels = []
        self.cumulative_gpa_labels = []
        self.cumulative_akts_labels = []
        self.overall_gpa_label = None

        self.create_ui()
        self.create_fixed_ui()
        self.create_management_buttons()  # new
        self.create_upload_button()
        self.calculate_all_gpa()

    def create_ui(self):
        """
        Arayüzü oluşturur.
        """
        self.main_frame = customtkinter.CTkScrollableFrame(self, label_text="Dersler ve Ortalama Hesaplama")
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame._label.configure(font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_frame.bind("<MouseWheel>", self.on_mousewheel)

        self.semester_frames = []
        self.semester_gpa_labels = []
        self.semester_akts_labels = []
        self.cumulative_gpa_labels = []
        self.cumulative_akts_labels = []

        row_num = 0
        for semester_index, semester_data in enumerate(self.semesters_data):
            semester_frame = customtkinter.CTkFrame(self.main_frame)
            semester_frame.grid(row=row_num, column=0, padx=10, pady=20, sticky="ew")
            semester_frame.grid_columnconfigure(1, weight=1)
            self.semester_frames.append(semester_frame)

            semester_label = customtkinter.CTkLabel(semester_frame, text=semester_data["semester"], font=customtkinter.CTkFont(weight="bold"))
            semester_label.grid(row=0, column=0, columnspan=4, pady=10)

            header_labels = ["Ders Kodu", "Ders Adı", "AKTS", "Harf Notu"]
            for col_num, header in enumerate(header_labels):
                header_label = customtkinter.CTkLabel(semester_frame, text=header, fg_color="#f0f0f0", text_color="black", corner_radius=6)
                header_label.grid(row=1, column=col_num, padx=5, pady=5, sticky="ew")

            course_row = 2
            for course_index, course in enumerate(semester_data["courses"]):
                code_label = customtkinter.CTkLabel(semester_frame, text=course["code"])
                code_label.grid(row=course_row, column=0, padx=5, pady=5, sticky="w")

                name_label = customtkinter.CTkLabel(semester_frame, text=course["name"], anchor="w")
                name_label.grid(row=course_row, column=1, padx=5, pady=5, sticky="ew")

                akts_label = customtkinter.CTkLabel(semester_frame, text=str(course["akts"]))
                akts_label.grid(row=course_row, column=2, padx=5, pady=5)

                grade_var = tkinter.StringVar(value=course["grade"])
                grade_dropdown = customtkinter.CTkComboBox(
                    semester_frame,
                    values=self.grade_options,
                    variable=grade_var,
                    command=lambda grade, c_index=course_index, s_index=semester_index: self.update_grade(grade, c_index, s_index)
                )
                grade_dropdown.grid(row=course_row, column=3, padx=5, pady=5)

                course_row += 1

            semester_gpa_label = customtkinter.CTkLabel(semester_frame, text="Dönem Ortalaması: -", font=customtkinter.CTkFont(weight="bold"))
            semester_gpa_label.grid(row=course_row, column=0, columnspan=2, pady=(25,3), sticky="w")
            self.semester_gpa_labels.append(semester_gpa_label)

            total_semester_akts = sum([c["akts"] for c in semester_data["courses"]])
            semester_akts_label = customtkinter.CTkLabel(
                semester_frame,
                text=f"Bu dönemdeki toplam AKTS: {total_semester_akts} / Bu dönem alınan AKTS: -"
            )
            semester_akts_label.grid(row=course_row, column=2, columnspan=2, pady=5, sticky="e")
            self.semester_akts_labels.append(semester_akts_label)

            cumulative_gpa_label = customtkinter.CTkLabel(semester_frame, text="Genel Ortalama: -", font=customtkinter.CTkFont(weight="bold"))
            cumulative_gpa_label.grid(row=course_row + 1, column=0, columnspan=2, pady=5, sticky="w")
            self.cumulative_gpa_labels.append(cumulative_gpa_label)

            cumulative_akts_label = customtkinter.CTkLabel(
                semester_frame,
                text="Alınan Toplam AKTS: -", font=customtkinter.CTkFont(weight="bold")
            )
            cumulative_akts_label.grid(row=course_row + 1, column=2, columnspan=2, pady=5, sticky="e")
            self.cumulative_akts_labels.append(cumulative_akts_label)

            row_num += 1

    def create_fixed_ui(self):
        """
        Sabit arayüz elemanlarını oluşturur.
        """
        fixed_frame = customtkinter.CTkFrame(self)
        fixed_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        fixed_frame.grid_columnconfigure(0, weight=1)
        fixed_frame.grid_columnconfigure(1, weight=1)

        self.overall_gpa_label = customtkinter.CTkLabel(fixed_frame, text="Toplam Genel Ortalama: -", font=customtkinter.CTkFont(weight="bold", size=16))
        self.overall_gpa_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.save_button = customtkinter.CTkButton(fixed_frame, text="CSV Olarak Kaydet", command=self.save_csv_file)
        self.save_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def create_upload_button(self):
        """
        CSV yükleme butonunu oluşturur.
        """
        upload_button = customtkinter.CTkButton(self, text="CSV Dosyası Yükle", command=self.upload_csv_data)
        upload_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def upload_csv_data(self):
        """
        CSV dosyasından veri yükleme işlemini gerçekleştirir.
        """
        file_path = ask_open_csv(get_courses_data)
        if file_path:
            try:
                self.semesters_data = get_courses_data()  # Varsayılan veriye sıfırla
                self.semesters_data = load_data_csv(file_path, get_courses_data)
                self.current_file = file_path  # Mevcut dosya yolunu güncelle
                self.recreate_ui()
                self.calculate_all_gpa()
                print(f"CSV dosyasından veriler yüklendi: {file_path}")
                tkinter.messagebox.showinfo("Başarılı", f"CSV dosyasından veriler yüklendi: {file_path}")
            except Exception as e:
                tkinter.messagebox.showerror("Hata", f"CSV dosyası yüklenirken hata oluştu: {e}")

    def update_grade(self, grade, course_index, semester_index):
        """
        Seçilen dersin notunu günceller.

        Args:
            grade (str): Seçilen not.
            course_index (int): Dersin indeksi.
            semester_index (int): Dönemin indeksi.
        """
        self.semesters_data[semester_index]["courses"][course_index]["grade"] = grade
        self.calculate_all_gpa()

    def save_csv_file(self):
        """
        CSV dosyasını kaydetme işlemini başlatır.
        """
        ask_save_csv(self.semesters_data)
        
    def recreate_ui(self):
        """
        Arayüzü yeniden oluşturur.
        """
        for frame in self.semester_frames:
            frame.destroy()
        self.semester_frames = []
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.create_ui()

    def calculate_all_gpa(self):
        """
        Tüm GPA değerlerini hesaplar ve arayüzü günceller.
        """
        cumulative_gpa, semester_gpas, _, semester_graded_akts_list, semester_total_akts_list = calculate_cumulative_gpa(
            self.semesters_data, self.grade_points
        )

        cumulative_up_to_semester_weighted_sum = 0
        cumulative_up_to_semester_akts = 0

        for i in range(len(semester_gpas)):
            for course in self.semesters_data[i]["courses"]:
                grade = course["grade"]
                if grade != "":
                    akts = int(course["akts"])
                    grade_point = self.grade_points.get(grade, 0.0)
                    cumulative_up_to_semester_akts += akts
                    cumulative_up_to_semester_weighted_sum += grade_point * akts

            if cumulative_up_to_semester_akts > 0:
                semester_cumulative_gpa = cumulative_up_to_semester_weighted_sum / cumulative_up_to_semester_akts
            else:
                semester_cumulative_gpa = 0.0

            if i < len(self.semester_gpa_labels):
                self.semester_gpa_labels[i].configure(text=f"Dönem Ortalaması: {semester_gpas[i]:.4f}")
            if i < len(self.semester_akts_labels):
                self.semester_akts_labels[i].configure(
                    text=f"Bu dönemdeki toplam AKTS: {semester_total_akts_list[i]} / Bu dönem alınan AKTS: {semester_graded_akts_list[i]}"
                )
            if i < len(self.cumulative_gpa_labels):
                self.cumulative_gpa_labels[i].configure(text=f"Genel Ortalama: {semester_cumulative_gpa:.4f}")
            if i < len(self.cumulative_akts_labels):
                self.cumulative_akts_labels[i].configure(text=f"Alınan Toplam AKTS: {cumulative_up_to_semester_akts}")

        self.overall_gpa_label.configure(text=f"Toplam Genel Ortalama: {cumulative_gpa:.4f}")
        
    def create_management_buttons(self):
        button_frame = customtkinter.CTkFrame(self, fg_color="transparent")  # Arka plan rengini kaldır
        button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        # Grid yapılandırması - iki eşit sütun
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Ders Ekle butonu - sol yarı
        add_course_button = customtkinter.CTkButton(
            button_frame, 
            text="Yeni Ders Ekle", 
            command=self.show_add_course_dialog
        )
        add_course_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        # Ders Sil butonu - sağ yarı
        remove_course_button = customtkinter.CTkButton(
            button_frame, 
            text="Ders Sil", 
            command=self.show_remove_course_dialog
        )
        remove_course_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def show_add_course_dialog(self):
        dialog = AddCourseDialog(self)
        self.wait_window(dialog)
        self.recreate_ui()

    def add_course(self, semester, code, name, akts):
        for sem_data in self.semesters_data:
            if sem_data["semester"] == semester:
                sem_data["courses"].append({
                    "code": code,
                    "name": name,
                    "akts": int(akts),
                    "grade": ""
                })
                break
        self.calculate_all_gpa()


    def show_remove_course_dialog(self):
        if not any(sem_data['courses'] for sem_data in self.semesters_data):
            tkinter.messagebox.showinfo("Bilgi", "Silinecek ders bulunamadı!")
            return
        
        dialog = RemoveCourseDialog(self)
        self.wait_window(dialog)
        self.recreate_ui()

    def remove_course(self, semester, code):
        for sem_data in self.semesters_data:
            if sem_data["semester"] == semester:
                sem_data["courses"] = [
                    course for course in sem_data["courses"] 
                    if course["code"] != code
                ]
                break
        self.calculate_all_gpa()
            
    def on_mousewheel(self, event):
        """
        Fare tekerleği ile kaydırma olayını yönetir.
        """
        scroll_amount = -1 * (event.delta // 40)
        self.main_frame._parent_canvas.yview_scroll(scroll_amount, "units")

    def run(self):
        """
        Uygulamayı başlatır.
        """
        self.mainloop()