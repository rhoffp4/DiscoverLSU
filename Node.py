class Node:
    def __init__(self,identifier):
        self.data = identifier
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
    def __init__(self,dataval = None):
        self.headval = dataval

    def setHead(self,node : Node):
        self.headval = node

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode: Node = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def Atbegining(self, data_in):
         NewNode = Node(data_in)
         NewNode.next = self.head
         self.head = NewNode

    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None
        
    def AtEnd(self, newdata):
            NewNode = Node(newdata)
            if self.headval is None:
                self.headval = NewNode
                return
            laste = self.headval
            while (laste.nextval):
                laste = laste.nextval
            laste.nextval = NewNode
