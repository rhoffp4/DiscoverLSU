from Mentor import Faculty
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

    def FindAllByCollege(self,TargetCollege = str("")):
        ReturnList = []
        TraversalNode = self.head
        while (TraversalNode is not None):
            if( TraversalNode.data.getCollege().upper() == TargetCollege.upper()):
                ReturnList.append(TraversalNode.data)

            TraversalNode = TraversalNode.next

        return ReturnList

    def FindAllByDepartment(self,TargetDepartment = str("")):
        ReturnList = []
        TraversalNode = self.head
        while (TraversalNode is not None):
            if( TraversalNode.data.getDepartment().upper() == TargetDepartment.upper()):
                ReturnList.append(TraversalNode.data)

            TraversalNode = TraversalNode.next

        return ReturnList




def __main__():
    print("Hello")
    MentorA = Faculty()
    MentorA.setName("AALEX")
    print(MentorA.getName())
    MentorB = Mentor()
    MentorB.setName("Sam")
    print(MentorB.getName())
    print(MentorA.getName())
    #Linked List testing
    List = Linkedlist()
    HeadNode = Node(MentorA)
    List.setHead(HeadNode)
    List.listprint()
    List.AtEnd(MentorB)
    List.listprint()
    MentorC = List.FindNodeByName("Sam")
    print(MentorC.getName())
    List.RemoveNodebyName("Sam")
    List.listprint()
    List.AtEnd(MentorB)
    List.AtEnd(MentorC)
    List.listprint()
    DisplayAllByTarget(List)

if __name__ == '__main__':
    __main__()

#find by department,college
