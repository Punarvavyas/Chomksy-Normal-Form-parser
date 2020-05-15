import sys
msg = sys.stdin.readlines()
print(msg)
parse=''

for i in range(0,len(msg)):
    parse= parse + msg[i] + " "
#parse= str(input("Give parse tree:\n"))
#parse=" (S (WNP (WDT (WRB How) (JJ many)) (NN students)) (VP (BE are) (VB (VBG taking) (NP (NN CSCI) (NN 1108)))))"
print("jj",parse)
