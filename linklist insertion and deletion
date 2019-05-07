class Node:
  def __init__(self,data):
    self.data=data
    self.nextt=None
class SLL:
  def __init__(self):
    self.head=None
  def insertAtBeg(self,data):
    temp=Node(data)
    temp.nextt=self.head
    self.head=temp 
  def delAtBeg(self):
    temp=self.head
    self.head=self.head.nextt
    temp.nextt=None   
  def printlist(self):
    temp=self.head
    while temp!=None:
      print(temp.data,"==>",end='')
      temp=temp.nextt
    print("None")
obj=SLL()
ch=0
while ch!=4:
  print("linked list implementataion\n","1.insertion in the beganning 2.deletion 3.print linked list 4.exit")
  ch=int(input())
  if ch==1:
    print("enter value of node")
    data=input()
    obj.insertAtBeg(data)
  elif ch==2:
    obj.delAtBeg()
    obj.printlist()  
    
  elif ch==3:
    obj.printlist()
      
