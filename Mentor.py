class Faculty:      #class name
    def __init__(self): #Constructor method
        self.name = str("")
        self.email = str("")
        self.students = str("")
        self.university = str("")
        self.college = str("")
        self.department = str("")

    def getName(self): # Getter method
        return str(self.name)

    def getEmail(self): #Getter method
        return str(self.email)

    def getStudents(self): #Getter method
        return str(self.students)

    def getUniversity(self): #Getter method
        return str(self.university)

    def getCollege(self): #Getter method
        return str(self.college)

    def getDepartment(self): #Getter method
        return str(self.department)

    def setName(self, name = ""): #Setter method
        self.name = str(name)

    def setEmail(self, email = ""): #Setter method
        self.email = str(email)

    def setStudents(self, students = ""): #Setter method
        self.students = str(students)

    def setUniversity(self, university = ""): #Setter method
        self.university = str(university)

    def setCollege(self, college = ""): #Setter method
        self.college = str(college)

    def setDepartment(self, department = ""): #Setter method
        self.department = str(department)        

a = Faculty()
a.setEmail("azimme9@lsu.edu")
print(a)

