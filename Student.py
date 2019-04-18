#Susan Borne

from Mentor import Faculty
from EventProfile import EventProfile
'''
Student class for lSU Discover Application
'''

class Student: #class name

    def __init__(self): #constructor method
        self.name = None
        self.email = None
        self.major = None
        self.minor = None
        self.mentor = []
        self.maybeGradDate = None
        self.actualGradDate = None
        self.durp = None
        self.activity = []

    def getname(self):
        if self.name is not None:
            return str(self.name)
        else:
            return "EMPTY"

    def getemail(self):
        if self.email is not None:
            return str(self.email)
        else:
            return "EMPTY"

    def getmajor(self):
        if self.major is not None:
            return str(self.major)
        else:
            return "EMPTY"

    def getminor(self):
        if self.minor is not None:
            return str(self.minor)
        else:
            return "EMPTY"

    def findmentor(self, name = str("")):
        flag: bool = False
        if isinstance(name,str):
            if self.mentor is not None:
                for mentor in self.mentor:
                    if mentor.getname().upper() == name.upper():
                        flag = True
                        return mentor

            else:
                return "EMPTY"
        else:
            return "EMPTY"
        if not flag:
            return "Does Not Exist"

    def getmentors(self):
        if self.mentor is not None:
            return self.mentor
        else:
            return "EMPTY"

    def getmaybegraddate(self):
        if self.maybeGradDate is not None:
           return self.maybeGradDate
        else:
            return "EMPTY"

    def getactualgraddate(self):
        if self.actualGradDate is not None:
            return self.actualGradDate
        else:
            return "EMPTY"

    def getdurp(self):
        if self.durp is not None:
            return self.durp
        else:
            return "EMPTY"

    def findactivity(self,name = str("")):
        flag : bool = False
        if self.activity is not None:
            if isinstance(name,str):
                for activity in self.activity:
                    if activity.getname().upper() == name.upper():
                        flag = True
                        return activity
            else:
                return "EMPTY"
        else:
            return "EMPTY"
        if flag == False:
            return "Does Not Exist"

    def getactivities(self):
        if self.activity is not None:
            return self.activity
        else:
            return "EMPTY"

    def setname(self, name = None):
        if isinstance(name,str):
            self.name = name

    def setemail(self, email = None):
        if isinstance(email,str):
            self.email = email

    def setmajor(self, major = None):
        if isinstance(major,str):
            self.major = major

    def setminor(self, minor = None):
        self.minor = minor

    def addmentor(self, mentor = None):
        if isinstance(mentor,Faculty):
            self.mentor.append(mentor)

    def setmaybegraddate(self, year1 = None):
        if isinstance(year1,str):
            self.maybeGradDate = year1

    def setactualgraddate(self, year2 = None):
        if isinstance(year2, str):
            self.actualGradDate = year2

    def setdurp(self, durp = None):
        if isinstance(durp,str):
            self.durp = durp

    def addactivity(self, activity = None):
        if isinstance(activity,EventProfile):
            self.activity.append(activity)

    def tostring(self):
        returnstring = ""
        print("inside tostring")
        if self.name is not None:
            returnstring += self.name + "\n"
        else:
            returnstring += "EMPTY\n"
        if self.email is not None:
            returnstring += self.email + "\n"
        else:
            returnstring += "EMPTY\n"
        if self.major is not None:
            returnstring += self.major + "\n"
        else:
            returnstring += "EMPTY\n"
        if self.minor is not None:
            returnstring += self.minor + "\n"
        else:
            returnstring += "EMPTY\n"
        returnstring += str(len(self.mentor)) + "\n"
        if len(self.mentor) > 0:
            for each in self.mentor:
                returnstring += each.getname() + "\n"

        if self.maybeGradDate is not None:
            returnstring += self.getmaybegraddate() + "\n"
        else:
            returnstring += "EMPTY\n"
        if self.actualGradDate is not None:
            returnstring += self.actualGradDate + "\n"
        else:
            returnstring += "EMPTY\n"
        if self.durp is not None:
            returnstring += self.durp + "\n"
        else:
            returnstring += "EMPTY\n"
        returnstring += str(len(self.activity)) + "\n"
        count = 0
        if len(self.activity) > 0:
            for each in self.activity:
                count += 1
                if count == len(self.activity):
                    returnstring += each.getname()
                else:
                    returnstring += each.getname() + "\n"
        return returnstring




def __main__():
    Alex = Student()
    Alex.setname("Alex Mensen-Johnson")
    print(Alex.getname())
    Alex.setemail("amense1@lsu.edu")
    print(Alex.getemail())
    Alex.setmajor("ComputerScience")
    print(Alex.getmajor())
    Alex.setminor("Business")
    print(Alex.getminor())
    Pujan = Faculty()
    Pujan.setname("Pujan Shrestha")
    Peter = Faculty()
    Peter.setname("Peter Wolenski")
    Alex.addmentor(Pujan)
    Alex.addmentor(Peter)
    list = Alex.getmentors()
    for mentor in list:
        print(mentor.getname())
    Alex.setmaybegraddate("05/05/2020")
    print(Alex.getmaybegraddate())
    Alex.setactualgraddate("05/05/2020")
    print(Alex.getactualgraddate())
    Alex.setdurp("durp")
    print(Alex.getdurp())
    Almighty = EventProfile()
    ICC = EventProfile()
    Almighty.setName("Almighty")
    ICC.setName("ICC")
    Alex.addactivity(Almighty)
    Alex.addactivity(ICC)
    MentorClone = Alex.findmentor("Peter Wolenski")
    print(MentorClone.getname())
    EventClone = Alex.findactivity("ICC")
    print(EventClone.getname())
    print(type(Alex))
    print(Alex.tostring())

if __name__ == '__main__':
    __main__()
