#Samuel Okoye
'''
Faculty Class for Lsu Discover
created by _____________(FIll IN LATER)
v1.0
v1.1 changelog
students data changed to list
new method for adding students
new method for deleting students
new method for fetching student list
Faculty Class object for LSU Discover Application
'''
class Faculty:      #class name
    def __init__(self): #Constructor method
        self.name = str("EMPTY")
        self.email = str("EMPTY")
        self.students = []
        self.university = str("EMPTY")
        self.college = str("EMPTY")
        self.department = str("EMPTY")

    def setname(self,name = str("")): # Method to set Student Name
        if isinstance(name,str):
            self.name = name

    def getname(self): # Getter method
        if self.name is not None:
           return self.name

    def setemail(self,email = str("")): # setter method for email
        if isinstance(email,str):
            self.email = email

    def getemail(self): #Getter method
        if self.email is not None:
            return self.email

    def addstudent(self,studentname = str("")):
        if isinstance(studentname,str):
            self.students.append(studentname)
            self.students.sort()

    def deletestudent(self,targetname = str("")):
        if isinstance(targetname,str):
            self.students.remove(targetname)

    def getstudents(self):
        if self.students is not None:
            return self.students

    def setuniversity(self,uni = str("")):
        if isinstance(uni,str):
            self.university = uni

    def getuniversity(self):
        if self.university is not None:
            return self.university

    def setcollege(self,college = str("")):
        if isinstance(college,str):
            self.college = college

    def getcollege(self):
        if self.college is not None:
            return self.college

    def setdepartment(self,department):
        if isinstance(department,str):
            self.department = department

    def getdepartment(self):
        if self.department is not None:
            return self.department

    #ToSting Method created for storage.py
    @property
    def tostring(self):
        returnstring: str = ""
        if self.name is not None:
            returnstring += (self.name + "\n")

        else:
            returnstring += ("EMPTY\n")

        if self.email is not None:
            returnstring += (self.email + "\n")

        else:
            returnstring += ("EMPTY\n")

        if self.students is not None:
            count = 0
            for studentname in self.students:
                count += 1

            returnstring += str(count) + "\n"
            for studentname in self.students:
                returnstring += (studentname+"\n")

        else:
            returnstring += ("0\n")

        if self.university is not None:
            returnstring += (self.university + "\n")

        else:
            returnstring += ("EMPTY\n")

        if self.college is not None:
            returnstring += (self.college + "\n")

        else:
            returnstring += ("EMPTY\n")

        if self.department is not None:
            returnstring += (self.department + "\n")

        else:
            returnstring += ("EMPTY\n")

        return str(returnstring)



def __main__():
    alex = Faculty()
    alex.setname("Alex Mensen-Johnson")
    alex.setemail("amense1@lsu.edu")
    alex.addstudent("Sam")
    alex.addstudent("alex")
    alex.addstudent("susan")
    alex.deletestudent("Sam")
    alex.setuniversity("LSU")
    alex.setcollege("Engineering")
    alex.setdepartment("Computer Science")
    print(alex.tostring)
    pujan = Faculty()
    print(pujan.tostring)

if __name__ == '__main__':
    __main__()
