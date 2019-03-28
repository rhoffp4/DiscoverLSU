from Student import Student
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class LinkedList:
    def __init__(self,data = None):
        self.head = data

    def setHead(self,node : Node):
        self.head = node

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data.getName())
            printval = printval.next

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode: Node = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    def RemoveNodebyName(self, Removekey):
        CurrentNode = self.head
        PrevNode = Node("Arbitrary")
        if (self.head.data.getName() == Removekey):
            self.head = self.head.next
            CurrentNode.data = None
            CurrentNode = None

        while CurrentNode is not None:
            PrevNode = CurrentNode
            CurrentNode = CurrentNode.next
            if (CurrentNode.data.getName() == Removekey):
                PrevNode.next = CurrentNode.next
                CurrentNode = None
                return

            if (CurrentNode.next is None):
                print("Target value not in list")
                return



    def AtEnd(self, newdata):
            NewNode = Node(newdata)
            if self.head is None:
                self.head = NewNode
                return

            last = self.head
            while (last.next is not None):
                last = last.next

            last.next = NewNode

    def FindNodeByName(self,TargetValue = str("")):
        flag = False
        compareValue = self.head
        while (flag == False):
            if(compareValue.data.getName() == TargetValue):
                flag = True
                return compareValue.data

            if (compareValue.next is not None):
                compareValue = compareValue.next
            else:
                print("data does not exist")

    def FindAllByMajor(self,TargetMajor = str("")):
        ReturnList = []
        TraversalNode = self.head
        while (TraversalNode is not None):
            if( TraversalNode.data.getMajor().upper() == TargetMajor.upper()):
                ReturnList.append(TraversalNode.data)

            TraversalNode = TraversalNode.next

        return ReturnList





def DisplayAllByTarget(TargetList = LinkedList()):  # BE CAReFUL when using this, can return either a list or a student class or a string
    targetinput = input("Enter a selection for Searching [ Name ][ Major ]")
    if (targetinput.upper() == "NAME"):
        secondinput = input("Enter a Name: ")
        studentreturnvalue = TargetList.FindNodeByName(secondinput)
        if (studentreturnvalue is not None):
            print(studentreturnvalue.getName())
            print(studentreturnvalue.getEmail())
            print(studentreturnvalue.getMajor)

        else:
            print("Invalid Input")

    if (targetinput.upper() == "MAJOR"):
        valuelist = TargetList.FindAllByMajor(targetinput)
        for profile in valuelist:
            print(profile.getName())
            print(profile.getEmail())
            print(profile.getMajor())

    else:
        print("INvalid input")


def __main__():
    print("Hello")
    StudentA = Student()
    StudentA.setName("Alex")
    print(StudentA.getName())
    StudentB = Student()
    StudentB.setName("Sam")
    print(StudentB.getName())
    print(StudentA.getName())
    #Linked List testing
    List = LinkedList()
    HeadNode = Node(StudentA)
    List.setHead(HeadNode)
    List.listprint()
    List.AtEnd(StudentB)
    List.listprint()
    StudentC = List.FindNodeByName("Sam")
    print(StudentC.getName())
    List.RemoveNodebyName("Sam")
    List.listprint()
    List.AtEnd(StudentB)
    List.AtEnd(StudentC)
    List.listprint()
    DisplayAllByTarget(List)

if __name__ == '__main__':
    __main__()