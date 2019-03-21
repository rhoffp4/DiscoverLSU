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
     def __init__(self,data = None):
         self.head = data

     def setHead(self,node : Node):
         self.head = node

     def listprint(self):
         printval = self.head
         while printval is not None:
             print(printval.data)
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
             if self.head is None:
                 self.head = NewNode
                 return
             laste = self.head
             while (laste.next):
                 laste = laste.next
             laste.next = NewNode

list1 = LinkedList()
list1.head = Node("Mon")
event2 = Node("Tue")
event3 = Node("Wed")
 # Link first Node to second node
list1.head.next = event2
event2.next=event3
list1.Atbegining("Sun")
list1.AtEnd("Sat")
list1.Inbetween(list1.head.next,"Fri")

list1.listprint()

from Discover_Profile import EventProfile
from Discover_Profile import Mentor
from Discover_Profile import Student

