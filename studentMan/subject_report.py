from .models import *


class Subject_Report:
    def __init__(self, lop="", mon="", siSo=0, soLuongDat=0, tiLe=0):
        self.lop = lop
        self.mon = mon
        self.siSo = siSo
        self.soLuongDat = soLuongDat
        self.tiLe = tiLe

    def find_class_of_user(self, current_user_id):
        current_user = Teacher.objects.filter(TeacherID=current_user_id)
        if not current_user:
            current_user = Student.objects.filter(StudentID=current_user_id)
        current_user = current_user[0]
        current_class = current_user.ClassOfSchool
        return [current_class]

    def passed_a_subject(self, student, subject, semester):
        marks = Mark.objects.filter(StudentID_mark=student,
                                    year_mark=student,
                                    semester_mark=semester,
                                    SubjectID_mark=subject)
        print(len(marks))
        if len(marks) == 0:
            print(-1)
            return -1
        else:
            mark = marks[0]
            m = (mark.markFifteen + 2 * mark.markOne + 3 * mark.markFinal) / 6
            if m >= subject.approved_mark:
                return 1
            else:
                return 0

    def count_student_passed_a_subject(self, students, subject, semester):
        count = 0
        for student in students:
            checked = self.passed_a_subject(student, subject, semester)
            if checked == -1:
                return -1
            elif checked == 1:
                count += 1
        return count

    def report_to_show(self, current_user_id, class_name, subjects, semester, year):
        # find current class
        if class_name == "---":
            classes = self.find_class_of_user(current_user_id)
        else:
            classes = ClassOfSchool.objects.filter(ClassId=class_name, year__year=year)
        print(classes)
        print(subjects)
        if subjects == "---":
            subjects = Subject.objects.all()
        else:
            subjects = Subject.objects.filter(name=subjects)[0]

        subject_reports = []
        for c in classes:
            students_in_class = Student.objects.filter(ClassOfSchool=c)
            student_number = len(students_in_class)
            current_class = c.ClassId
            for subject in subjects:
                counted = self.count_student_passed_a_subject(students_in_class, subject, semester)
                if counted == -1:
                    continue
                else:
                    subject_reports.append(
                        Subject_Report(current_class, subject.name, student_number, counted,
                                       round((counted / student_number), 2)))
        return subject_reports
