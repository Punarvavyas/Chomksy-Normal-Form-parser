import re
import sys

print("The above code will not work only if multiple parse trees are given as input. The code will parse all the string except the first statement of assignment as it has multiple parse trees.")
print("If there are multiple lines in grammer write each line of grammer in a single line with each line seprated with space or you can copy paste the entire input as it is and then press Ctrl-D just make sure every line is in a different line. Then press Ctrl-D ")
print("These are lines for you to copy")
print("(S (WNP (WDT What) (NN courses)) (VP (BE are) (VP (VBN offered) (PP (IN in) (NN fall)))))")
print("(S (WNP (WDT (WRB How) (JJ many)) (NN students)) (VP (BE are) (VB (VBG taking) (NP (NN CSCI) (NN 1108)))))")
print("(S (NP dogs) (VP run) (ADV fast)) ")
print('Give the grammer:\n')

msg = sys.stdin.readlines()
#print(msg)

parse=''

for i in range(0,len(msg)):
    parse = parse + msg[i] + " "
   # print(parse)
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

class CustomLinkedList:
    def __init__(self):
        self.head = None

    def nodeallocation(self,new_data):

        new_node = Node(new_data)
        #print('First',new_node.data)

        if self.head is None:
            self.head = new_node
            return

    def pcnodeallocation(self,data1,data2):

        new_node = Node(data1)
        #print('Allocation',new_node.data)

        if data2.head.child1 is None:
            data2.head.child1=new_node
            new_node.parent= data2.head
            self.head=new_node
            #print(self.head)
        elif data2.head.child2 is None:
            data2.head.child2 = new_node
            new_node.parent = data2.head
            self.head = new_node

        else:
            print("Invalid CNF")
    def firstdealloc(self,data2):
        #print('HI', data2.head.data)
        self.head=data2.head.parent
        #print('h',data2.head.parent.data)
        #print('Deallocation',self.head.data)
llist = CustomLinkedList()


parselist=parse.split()
#print(parselist)

temp=[]
for i in parselist:


    if re.match(r'\([A-Z]+', i):
        if len(temp) == 0:
            llist.nodeallocation(i)

        elif len(temp) !=0 and llist.head.child2 is None:
            llist.pcnodeallocation(i,llist)
        elif len(temp) != 0 and re.match(r'[A-Za-z0-9]+\)+',temp[-1]) and llist.head.child2 is None:

            llist.nodeallocation(i)
        elif re.match(r'\([A-Z]+',temp[-1]):
         # print(temp[-1])
          llist.pcnodeallocation(i,llist)
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
