

class EventProfile: 
    def __init__(self):
        self.Name = str("")
        self.Date = int(0)
        self.Description = str("")
        self.Location = str("")
        self.Time = int(0)
        self.Attendence = str("")

    def getName(self):
        return self.Name
    
    def getDate(self):
        return int(self.Date)
    
    def getDescription(self):
        return str(self.Description)

    def getLocation(self):
        return str(self.Location)

    def getTime(self):
        return int(self.Time)

    def getAttendence(self):
        return str(self.Attendence)
    
    def setName(self,name):
        self.Name = name
        
    def setDate(self,Date = 0):
        self.Date = Date

    def setDescription(self,Description = 0):
        self.Description = Description

    def setLocation(self,Location = 0):
        self.Location = Location

    def setTime(self,Time = 0):
        self.Time = Time

    def setAttendence(self,Attendence = 0):
        self.Attendence = Attendence 


