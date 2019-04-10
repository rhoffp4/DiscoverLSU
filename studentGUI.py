# Susan Borne
# Alex Zimmerman

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 510)
        self.addStudent = QtWidgets.QLabel(Form)
        self.addStudent.setGeometry(QtCore.QRect(180, 30, 121, 16))
        self.addStudent.setObjectName("addStudent")
        self.student = QtWidgets.QLabel(Form)
        self.student.setGeometry(QtCore.QRect(31, 72, 48, 16))
        self.student.setObjectName("student")
        self.studentFirstBox = QtWidgets.QLineEdit(Form)
        self.studentFirstBox.setGeometry(QtCore.QRect(170, 60, 131, 21))
        self.studentFirstBox.setObjectName("studentFirstBox")
        self.studentLasrBox = QtWidgets.QLineEdit(Form)
        self.studentLasrBox.setGeometry(QtCore.QRect(320, 60, 121, 21))
        self.studentLasrBox.setObjectName("studentLasrBox")
        self.studentEmailBox = QtWidgets.QLineEdit(Form)
        self.studentEmailBox.setGeometry(QtCore.QRect(174, 103, 131, 21))
        self.studentEmailBox.setObjectName("studentEmailBox")
        self.collegeBox = QtWidgets.QComboBox(Form)
        self.collegeBox.setGeometry(QtCore.QRect(171, 132, 271, 26))
        self.collegeBox.setObjectName("collegeBox")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.collegeBox.addItem("")
        self.college = QtWidgets.QLabel(Form)
        self.college.setGeometry(QtCore.QRect(31, 134, 46, 16))
        self.college.setObjectName("college")
        self.majorBox = QtWidgets.QLineEdit(Form)
        self.majorBox.setGeometry(QtCore.QRect(172, 164, 131, 21))
        self.majorBox.setObjectName("majorBox")
        self.mentorLast = QtWidgets.QLabel(Form)
        self.mentorLast.setGeometry(QtCore.QRect(326, 246, 26, 16))
        self.mentorLast.setObjectName("mentorLast")
        self.studentFirst = QtWidgets.QLabel(Form)
        self.studentFirst.setGeometry(QtCore.QRect(172, 80, 27, 16))
        self.studentFirst.setObjectName("studentFirst")
        self.mentor = QtWidgets.QLabel(Form)
        self.mentor.setGeometry(QtCore.QRect(31, 226, 44, 16))
        self.mentor.setObjectName("mentor")
        self.studentEmail = QtWidgets.QLabel(Form)
        self.studentEmail.setGeometry(QtCore.QRect(31, 103, 121, 16))
        self.studentEmail.setObjectName("studentEmail")
        self.majors = QtWidgets.QLabel(Form)
        self.majors.setGeometry(QtCore.QRect(31, 164, 51, 16))
        self.majors.setObjectName("majors")
        self.majorBox2 = QtWidgets.QLineEdit(Form)
        self.majorBox2.setGeometry(QtCore.QRect(325, 164, 121, 21))
        self.majorBox2.setObjectName("majorBox2")
        self.minors = QtWidgets.QLabel(Form)
        self.minors.setGeometry(QtCore.QRect(31, 195, 51, 16))
        self.minors.setObjectName("minors")
        self.minorBox1 = QtWidgets.QLineEdit(Form)
        self.minorBox1.setGeometry(QtCore.QRect(172, 195, 131, 21))
        self.minorBox1.setText("")
        self.minorBox1.setObjectName("minorBox1")
        self.mentorEmail = QtWidgets.QLabel(Form)
        self.mentorEmail.setGeometry(QtCore.QRect(30, 270, 80, 16))
        self.mentorEmail.setObjectName("mentorEmail")
        self.antiGradDate = QtWidgets.QLabel(Form)
        self.antiGradDate.setGeometry(QtCore.QRect(30, 301, 135, 16))
        self.antiGradDate.setObjectName("antiGradDate")
        self.gradDate = QtWidgets.QLabel(Form)
        self.gradDate.setGeometry(QtCore.QRect(30, 332, 99, 16))
        self.gradDate.setObjectName("gradDate")
        self.activity = QtWidgets.QLabel(Form)
        self.activity.setGeometry(QtCore.QRect(30, 362, 105, 16))
        self.activity.setObjectName("activity")
        self.durp = QtWidgets.QLabel(Form)
        self.durp.setGeometry(QtCore.QRect(30, 393, 77, 16))
        self.durp.setObjectName("durp")
        self.minorBox2 = QtWidgets.QLineEdit(Form)
        self.minorBox2.setGeometry(QtCore.QRect(325, 195, 121, 21))
        self.minorBox2.setObjectName("minorBox2")
        self.lsuEdu = QtWidgets.QLabel(Form)
        self.lsuEdu.setGeometry(QtCore.QRect(310, 110, 56, 16))
        self.lsuEdu.setObjectName("lsuEdu")
        self.mentorFirst = QtWidgets.QLabel(Form)
        self.mentorFirst.setGeometry(QtCore.QRect(172, 246, 27, 16))
        self.mentorFirst.setObjectName("mentorFirst")
        self.mentorFirstBox = QtWidgets.QLineEdit(Form)
        self.mentorFirstBox.setGeometry(QtCore.QRect(172, 226, 131, 20))
        self.mentorFirstBox.setObjectName("mentorFirstBox")
        self.mentorLastBox = QtWidgets.QLineEdit(Form)
        self.mentorLastBox.setGeometry(QtCore.QRect(325, 226, 121, 20))
        self.mentorLastBox.setObjectName("mentorLastBox")
        self.studentLast = QtWidgets.QLabel(Form)
        self.studentLast.setGeometry(QtCore.QRect(320, 80, 26, 16))
        self.studentLast.setObjectName("studentLast")
        self.mentorEmailBox = QtWidgets.QLineEdit(Form)
        self.mentorEmailBox.setGeometry(QtCore.QRect(172, 270, 131, 21))
        self.mentorEmailBox.setObjectName("mentorEmailBox")
        self.antiGradScroll = QtWidgets.QDateEdit(Form)
        self.antiGradScroll.setGeometry(QtCore.QRect(172, 300, 110, 24))
        self.antiGradScroll.setObjectName("antiGradScroll")
        self.gradScroll = QtWidgets.QDateEdit(Form)
        self.gradScroll.setGeometry(QtCore.QRect(172, 330, 110, 24))
        self.gradScroll.setObjectName("gradScroll")
        self.activityBox = QtWidgets.QLineEdit(Form)
        self.activityBox.setGeometry(QtCore.QRect(172, 362, 131, 21))
        self.activityBox.setObjectName("activityBox")
        self.durpDropdown = QtWidgets.QComboBox(Form)
        self.durpDropdown.setGeometry(QtCore.QRect(172, 391, 141, 26))
        self.durpDropdown.setObjectName("durpDropdown")
        self.durpDropdown.addItem("")
        self.durpDropdown.addItem("")
        self.durpDropdown.addItem("")
        self.durpDropdown.addItem("")
        self.entryBox = QtWidgets.QDateTimeEdit(Form)
        self.entryBox.setGeometry(QtCore.QRect(172, 430, 194, 24))
        self.entryBox.setObjectName("entryBox")
        self.entryLabel = QtWidgets.QLabel(Form)
        self.entryLabel.setGeometry(QtCore.QRect(30, 430, 121, 16))
        self.entryLabel.setObjectName("entryLabel")
        self.Add = QtWidgets.QDialogButtonBox(Form)
        self.Add.setGeometry(QtCore.QRect(290, 460, 164, 32))
        self.Add.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Add.setObjectName("Add")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addStudent.setText(_translate("Form", "Student Information"))
        self.student.setText(_translate("Form", "Student"))
        self.mentorLast.setText(_translate("Form", "Last"))
        self.studentFirst.setText(_translate("Form", "First"))
        self.mentor.setText(_translate("Form", "Mentor"))
        self.studentEmail.setText(_translate("Form", "Username (Email)"))
        self.majors.setText(_translate("Form", "Major(s)"))
        self.minors.setText(_translate("Form", "Minor(s)"))
        self.mentorEmail.setText(_translate("Form", "Mentor Email"))
        self.antiGradDate.setText(_translate("Form", "Anticipated Grad Date"))
        self.gradDate.setText(_translate("Form", "Graduation Date"))
        self.activity.setText(_translate("Form", "Activity Attended"))
        self.durp.setText(_translate("Form", "DURP status"))
        self.lsuEdu.setText(_translate("Form", "@lsu.edu"))
        self.mentorFirst.setText(_translate("Form", "First"))
        self.studentLast.setText(_translate("Form", "Last"))
        self.durpDropdown.setItemText(0, _translate("Form", "select one:"))
        self.durpDropdown.setItemText(1, _translate("Form", "Candidate"))
        self.durpDropdown.setItemText(2, _translate("Form", "Awardee"))
        self.durpDropdown.setItemText(3, _translate("Form", "Not enrolled"))
        self.collegeBox.setItemText(0, _translate("Form", "Select One:"))
        self.collegeBox.setItemText(1, _translate("Form", "College of Agriculture"))
        self.collegeBox.setItemText(2, _translate("Form", "College of Art and Design"))
        self.collegeBox.setItemText(3, _translate("Form", "E.J. Ourso College of Business"))
        self.collegeBox.setItemText(4, _translate("Form", "College of the Coast & Environment"))
        self.collegeBox.setItemText(5, _translate("Form", "College of Engineering"))
        self.collegeBox.setItemText(6, _translate("Form", "College of Human Sciences & Education"))
        self.collegeBox.setItemText(7, _translate("Form", "College of Humanities & Social Sciences"))
        self.collegeBox.setItemText(8, _translate("Form", "Manship School of Mass Communication"))
        self.collegeBox.setItemText(9, _translate("Form", "College of Music & Dramatic Arts"))
        self.collegeBox.setItemText(10, _translate("Form", "College of Science"))
        self.collegeBox.setItemText(11, _translate("Form", "Ogden Honors College"))
        self.collegeBox.setItemText(12, _translate("Form", "University College"))
        self.college.setText(_translate("Form", "College"))
        self.entryLabel.setText(_translate("Form", "Entry Completed on"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

