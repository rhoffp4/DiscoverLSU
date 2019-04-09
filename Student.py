#Susan Borne

class Student: #class name
    def __init__(self): #constructor method
        self.name = str("")
        self.email = str("")
        self.major = str("")
        self.minor = str("")
        self.mentor = str("")
        self.mentorEmail = str("")
        self.maybeGradDate = str("")
        self.actualGradDate = str("")
        self.durp = str("")
        self.activity = str("")

    def getName(self):
        return str(self.name)

    def getEmail(self):
        return str(self.email)

    def getMajor(self):
        return str(self.major)

    def getMinor(self):
        return str(self.minor)

    def getMentor(self):
        return str(self.mentor)

    def getMentorEmail(self):
        return str(self.mentorEmail)

    def getMaybeGradDate(self):
        return str(self.maybeGradDate)

    def getActualGradDate(self):
        return str(self.actualGradDate)

    def getDurp(self):
        return str(self.durp)

    def getActivity(self):
        return str(self.activity)

    def setName(self, name = ""):
        self.name = name

    def setEmail(self, email = ""):
        self.email = email

    def setMajor(self, major = ""):
        self.major = major

    def setMinor(self, minor = ""):
        self.minor = minor

    def setMentor(self, mentor = ""):
        self.mentor = mentor

    def setMentorEmail(self, mEmail = ""):
        self.mentorEmail = mEmail

    def setMaybeGradDate(self, year1 = ""):
        self.maybeGradDate = year1

    def setActualGradDate(self, year2 = ""):
        self.actualGradDate = year2

    def setDurp(self, durp = ""):
        self.durp = durp

    def setActivity(self, activity = ""):
        self.activity = activity

a = Student()
a.setName(input("Enter name "))
a.setEmail(input("Enter email "))
a.setMajor(input("Enter major "))
a.setMinor(input("Enter minor "))
a.setMentor(input("Enter mentor "))
a.setMentorEmail(input("Enter mentor email "))
a.setMaybeGradDate(input("Enter anticipated graduation date "))
a.setActualGradDate(input("Enter actual graduation date "))
a.setDurp(input("Enter DURP status "))
a.setActivity(input("Enter activity name "))
print(a.getName())
print(a.getEmail())
print(a.getMajor())
print(a.getMinor())
print(a.getMentor())
print(a.getMentorEmail())
print(a.getMaybeGradDate())
print(a.getActualGradDate())
print(a.getDurp())
print(a.getActivity())
        
