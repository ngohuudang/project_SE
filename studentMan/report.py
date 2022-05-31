from .models import *


class Report:
    def __init__(self, lop="", siSo=0, soLuongDat=0, tiLe=0):
        self.lop = lop
        self.siSo = siSo
        self.soLuongDat = soLuongDat
        self.tiLe = tiLe

    def findClassID(self, currentID):
        currentUser = Teacher.objects.filter(TeacherID=currentID)
        if not currentUser:
            currentUser = Student.objects.filter(StudentID=currentID)
        currentUser = currentUser[0]
        classID = currentUser.ClassOfSchool.id
        return classID

    def countPassedSubject(self, student, semester):
        marks = Mark.objects.filter(StudentID_mark=student,
                                    year_mark=student,
                                    semester_mark=semester)
        count = 0
        for mark in marks:
            subject = Subject.objects.filter(SubjectID=mark.SubjectID_mark)[0]
            minMark = subject.approved_mark
            m = (mark.markFifteen + 2 * mark.markOne + 3 * mark.markFinal) / 6
            if m >= minMark:
                count += 1
        return count

    def passedSemester(self, student, semester):
        passedSubject = self.countPassedSubject(student, semester)
        if passedSubject == 9:
            return True
        else:
            False

    def passedRate(self, students, semester):
        count = 0
        for student in students:
            if self.passedSemester(student, semester):
                count += 1
        return [count, (count / len(students)) * 100]

    def createReport(self, classID, semester):
        students = Student.objects.filter(ClassOfSchool__id=classID)
        Lop = ClassOfSchool.objects.filter(id=classID)[0].ClassId
        passed_count, passed_rate = self.passedRate(students, semester)
        return Report(Lop, len(students), passed_count, passed_rate)

    def show(self, currentID, className, semester, year):
        if className == "---":
            classID = self.findClassID(currentID)
        else:
            classID = ClassOfSchool.objects.filter(ClassId=className, year__year=year)[0].id

        return self.createReport(classID, semester)
