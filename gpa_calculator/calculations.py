def calculate_semester_gpa(semester_data, grade_points):
    """
    Bir dönemin GPA'sını hesaplar.

    Args:
        semester_data (dict): Döneme ait ders verileri.
        grade_points (dict): Harf notu -> Not değeri eşlemeleri.

    Returns:
        tuple: (Dönem GPA'sı, notlandırılan AKTS toplamı, dönem toplam AKTS)
    """
    graded_akts = 0
    weighted_sum = 0
    for course in semester_data["courses"]:
        grade = course["grade"]
        if grade != "":
            akts = int(course["akts"])
            grade_point = grade_points.get(grade, 0.0)
            graded_akts += akts
            weighted_sum += grade_point * akts

    if graded_akts > 0:
        return weighted_sum / graded_akts, graded_akts, sum([int(c["akts"]) for c in semester_data["courses"]])
    return 0.0, 0, sum([int(c["akts"]) for c in semester_data["courses"]])

def calculate_cumulative_gpa(semesters_data, grade_points):
    """
    Kümülatif GPA'yı hesaplar.

    Args:
        semesters_data (list): Tüm dönemlere ait ders verileri.
        grade_points (dict): Harf notu -> Not değeri eşlemeleri.

    Returns:
        tuple: (kümülatif GPA, dönem GPA'ları listesi, toplam AKTS,
                dönem notlandırılan AKTS listesi, dönem toplam AKTS listesi)
    """
    cumulative_weighted_sum = 0
    cumulative_akts = 0
    semester_gpas = []
    semester_graded_akts_list = []
    semester_total_akts_list = []

    for semester_data in semesters_data:
        semester_gpa, semester_graded_akts, semester_total_akts = calculate_semester_gpa(semester_data, grade_points)
        semester_gpas.append(semester_gpa)
        semester_graded_akts_list.append(semester_graded_akts)
        semester_total_akts_list.append(semester_total_akts)

        for course in semester_data["courses"]:
            grade = course["grade"]
            if grade != "":
                akts = int(course["akts"])
                grade_point = grade_points.get(grade, 0.0)
                cumulative_akts += akts
                cumulative_weighted_sum += grade_point * akts

    if cumulative_akts > 0:
        cumulative_gpa = cumulative_weighted_sum / cumulative_akts
    else:
        cumulative_gpa = 0.0

    return cumulative_gpa, semester_gpas, cumulative_akts, semester_graded_akts_list, semester_total_akts_list