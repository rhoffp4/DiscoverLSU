from Student import Student
from Mentor import Faculty
# from Node import Node,LinkedList

from EventProfile import EventProfile

'''
basic storage class, creates txt files and stores them and reads them later on
v1.0
Alex Mensen-Johnson
Reads Contents of Data in simple formating and represents data in storage.
File stores strings by line
'''

class Storage:
    def __init__(self):
        self.Studentfilename = "/Users/idky/PycharmProjects/BasicProject/Math4020/StudentStorageFile.txt" #Student Storage
        self.file = None #file to be opened
        self.filesize = None# size of file
        self.overwritedatasize = None #size of overwrite file
        self.linelimit = 10 #current Line limit of text file
        self.dataseperator = ':'#current data seperator
        self.fileindex = None#index of file
        self.overwritedata = ""#overwrite data
        self.fileexist = None
        self.filesaveexist = None
        self.filedata = None

    def getname(self):
        return self.Studentfilename

    def fileclear(self):
        self.file = open(self.Studentfilename, "w")# becareful! clears existing data
        print("Clearing....")
        self.file.truncate(0)
        self.file.close()

    def filewrite(self):# becarefule! overwrites existing data
        print("Overwriting..")
        file = open(self.Studentfilename, "w")
        self.fileclear()
        file.write(self.overwritedata)
        print("File saved!")
        file.close()

    def addtowrite(self,stringarray = None):
        if (stringarray == None):
            raise Exception("Storage.Filewrite: input is type None")
            return False
        else:
            count = 0
            lines = 0
            for word in stringarray:
                if (count == self.linelimit):
                    word = '\n' + word + self.dataseperator
                    lines +=1
                else:
                    word = word + self.dataseperator  # prepping for storage, colons will be used to seperate the file
                self.overwritedata += word
                count += 1

    def fileread(self):
        self.file = open(self.Studentfilename, "r")
        self.filedata = self.file.read().split(self.dataseperator)
        self.file.close()
        return self.filedata

    def StudentSave(self, truant = None):
        if type(truant) != type(Student()):
            raise Exception("Storage.StudentSave: input is not type object ")
        else:
            temp = truant.tostring()
            array = temp.splitlines()
            self.addtowrite(array)

    def StudentLoad(self): # returns array of students
        if (self.filedata == None):
            self.fileread()
        rtrndata = []
        temp = Student()
        for i in range(len(self.filedata)):
            temp.setname(self.filedata[i])
            i += 1
            temp.setemail(self.filedata[i])
            i += 1
            temp.setmajor(self.filedata[i])
            i += 1
            temp.setminor(self.filedata[i])
            i += 1
            counter = int(self.filedata[i])
            i += 1
            for j in range(counter):
                prof = Faculty()
                prof.setname(self.filedata[i])
                temp.addmentor(prof)
                i += 1
            temp.setmaybegraddate(self.filedata[i])
            i += 1
            temp.setactualgraddate(self.filedata[i])
            i += 1
            temp.setdurp(self.filedata[i])
            i += 1
            counter = int(self.filedata[i])
            i += 1
            for l in range(counter):
                event = EventProfile()
                event.setname(self.filedata[i])
                i += 1
                temp.addactivity()
            rtrndata.append(temp)
        return rtrndata

    # def MentorDataRead(self):


def __main__():
    Alex = Student()
    Alex.setname("Alex Mensen-Johnson")
    Alex.setemail("amense1@lsu.edu")
    Alex.setmajor("ComputerScience")
    Alex.setminor("Business")
    Pujan = Faculty()
    Pujan.setname("Pujan Shrestha")
    Peter = Faculty()
    Peter.setname("Peter Wolenski")
    Alex.addmentor(Pujan)
    Alex.addmentor(Peter)
    Alex.setmaybegraddate("05/05/2020")
    Alex.setactualgraddate("05/05/2020")
    Alex.setdurp("durp")
    Almighty = EventProfile()
    ICC = EventProfile()
    Almighty.setname("Almighty")
    ICC.setname("ICC")
    Alex.addactivity(Almighty)
    Alex.addactivity(ICC)
    vault = Storage()
    vault.StudentSave(Alex)
    vault.filewrite()
    print(vault.fileread())
    


if __name__ == '__main__':
    __main__()
