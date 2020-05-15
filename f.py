import re
import sys
msg = sys.stdin.readlines()
print(msg)
parse=''
cv=0
for i in range(0,len(msg)):
    parse = parse + msg[i] + " "
#parse= str(input("Give parse tree:\n"))
#parse=" (S (WNP (WDT (WRB How) (JJ many)) (NN students)) (VP (BE are) (VB (VBG taking) (NP (NN CSCI) (NN 1108)))))"
val=''
#print("jj",parse)
class Node:


    def __init__(self, data):
        self.data = data
        self.child1 = None
        self.child2 = None
        self.parent= None
cnt = 0
class CustomLinkedList:
    def __init__(self):
        self.head = None

    def nodeallocation(self,new_data):

        new_node = Node(new_data)
        #print('First',new_node.data)

        if self.head is None:
            self.head = new_node
            return

    def pcnodeallocation(self, data1, data2):

        new_node = Node(data1)
        #print('Allocation',new_node.data)
        #cnt =0
        if data2.head.child1 is None:
            data2.head.child1=new_node
            new_node.parent= data2.head
            self.head=new_node
            #print(self.head)
        elif data2.head.child2 is None:
            data2.head.child2 = new_node
            new_node.parent = data2.head
            self.head = new_node
            global cnt
            cnt=cnt+1

        else:
            print("Invalid CNF")
    def firstdealloc(self,data2):
        #print('HI', data2.head.data)
        ls1=[]
        global cv
        self.head=data2.head.parent
        if self.head.data in ls1:
            cv=cv+1
        else:
         ls1.append(self.head.data)
         cv=cv+1


        #print('h',data2.head.parent.data)
        #print('Deallocation',self.head.data)
llist = CustomLinkedList()


parselist=parse.split()
print(parselist)

temp=[]

for i in parselist:


    if re.match(r'\([A-Z]+', i):
        if len(temp) == 0:
            llist.nodeallocation(i)

        elif len(temp) !=0 and llist.head.child2 is None:
            llist.pcnodeallocation(i,llist)
            if llist.head.parent is not None:
                cnt=cnt+1
                print(cnt,'sss')
                #temp=[]
        elif len(temp) != 0 and re.match(r'[A-Za-z0-9]+\)+',temp[-1]) and llist.head.parent is None and llist.head.child2 is not None and llist.head.child1 is not  None and cv == 2:
            llist = CustomLinkedList()
            print('hi')
            temp=[]
            llist.nodeallocation(i)
        elif re.match(r'\([A-Z]+', temp[-1]):
            # print(temp[-1])
            llist.pcnodeallocation(i, llist)
        else:
            val="Invalid"
           # print("Invalid")
            break
    elif re.match(r'[A-Za-z0-9]+\)+',i):
            #print(i)
            count=0
            for a in i:
               # print(a)
                if a == ')' and llist.head.parent is not None :
                    llist.firstdealloc(llist)
                    #count=count+1
                else:
                    continue



    temp.append(i)


if len(val) == 0:
        print("Valid CNF trees")
else:
        print("Invalid CNF trees")
#print(temp)
