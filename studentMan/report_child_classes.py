from .report_parent_class import *


class Semester_Report(Report):

    def count_passed_subject(self, student, semester, subject_num):
        marks = Mark.objects.filter(student=student,
                                    semester_mark=semester)
        if len(marks) != subject_num:
            return -1
        count = 0
        for mark in marks:
            subject = Subject.objects.filter(SubjectID=mark.subject)[0]
            checked = self.check_passed(mark, subject)
            if checked == -1:
                return -1
            else:
                count += checked
        return count

    def count_passed_student(self, students, semester, subject_number):
        count = 0
        for student in students:
            checked = self.count_passed_subject(student, semester, subject_number)
            if checked == -1:
                return -1
            elif checked == subject_number:
                count += 1
        return count

    def report_to_show(self, user, class_id, semester, year, subject_number):
        if class_id == "---":
            classes = self.find_class_of_user(user)
        else:
            classes = ClassOfSchool.objects.filter(classId=class_id, year__year=year)

        reports = []
        for c in classes:
            students = Student.objects.filter(classOfSchool=c)
            passed_number = self.count_passed_student(students, semester, subject_number)
            total_student = len(students)
            if passed_number == -1 or total_student == 0:
                continue

            reports.append(
                Semester_Report(c.classId,
                                total_student,
                                passed_number,
                                round(passed_number * 100 / total_student, 2)))
        return reports


class Subject_Report(Report):
    def __init__(self, class_id="", subject="", student_number=0, passed_number=0, passed_rate=0):
        self.class_id = class_id
        self.subject = subject
        self.student_number = student_number
        self.passed_number = passed_number
        self.passed_rate = passed_rate

    def check_if_passed_subjects(self, student, subject, semester):
        mark = Mark.objects.filter(student=student,
                                   subject=subject,
                                   semester_mark=semester)
        if len(mark) == 0:
            return -1
        mark = mark[0]
        return self.check_passed(mark, subject)

    def count_student_passed_a_subject(self, students, subject, semester):
        count = 0
        for student in students:
            checked = self.check_if_passed_subjects(student, subject, semester)
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
            classes = ClassOfSchool.objects.filter(classId=class_name, year__year=year)
        if subjects == "---":
            subjects = Subject.objects.all()
        else:
            subjects = Subject.objects.filter(name=subjects)

        reports = []
        for c in classes:
            students_in_class = Student.objects.filter(classOfSchool=c)
            student_number = len(students_in_class)
            if student_number == 0:
                continue
            current_class = c.classId
            for subject in subjects:
                counted = self.count_student_passed_a_subject(students_in_class, subject, semester)
                if counted == -1:
                    continue
                else:
                    reports.append(
                        Subject_Report(current_class, subject.name, student_number, counted,
                                       round((counted / student_number) * 100, 2)))
        return reports
