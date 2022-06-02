from .models import *


class Report:
    def __init__(self, lop="", siSo=0, soLuongDat=0, tiLe=0):
        self.lop = lop
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

    def count_passed_subject(self, student, semester, subject_num):
        marks = Mark.objects.filter(StudentID_mark=student,
                                    year_mark=student,
                                    semester_mark=semester)
        print(len(marks))
        print(subject_num)
        if len(marks) != subject_num:
            return -1
        count = 0
        for mark in marks:
            if (mark.markFifteen == None) or (mark.markOne == None) or (mark.markFinal == None):
                return -1
            subject = Subject.objects.filter(SubjectID=mark.SubjectID_mark)[0]
            min_mark = subject.approved_mark
            m = (mark.markFifteen + 2 * mark.markOne + 3 * mark.markFinal) / 6
            if m >= min_mark:
                count += 1
        return count

    def passed_rate(self, students, semester, subject_number):
        count = 0
        for student in students:
            counted = self.count_passed_subject(student, semester, subject_number)
            if counted == -1:
                return -1, -1
            if counted == subject_number:
                count += 1
        return count, (count / len(students)) * 100

    def report_to_show(self, current_user_id, class_name, semester, year, subject_num):
        # find current class
        if class_name == "---":
            classes = self.find_class_of_user(current_user_id)
        else:
            classes = ClassOfSchool.objects.filter(ClassId=class_name, year__year=year)

        reports = []
        for c in classes:
            # find all student in that class
            students_in_class = Student.objects.filter(ClassOfSchool=c)
            student_number = len(students_in_class)

            current_class = c.ClassId
            passed_num, passed_rate = self.passed_rate(students_in_class, semester, subject_num)
            if passed_num == -1:
                continue
            reports.append(Report(current_class, student_number, passed_num, round(passed_rate, 2)))
        return reports
