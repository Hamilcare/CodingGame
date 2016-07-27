import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

tabAdja = []
tabGateway = []
for i in range(n):
    tabAdja.append([])
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    tabAdja[n1].append(n2)
   
print("tabAdja "+str(tabAdja), file=sys.stderr)

#Update tabAdja
for i in range(len(tabAdja)):
    for j in range(len(tabAdja[i])):
        tempo=tabAdja[i][j]
        if(i not in tabAdja[tempo]):
            tabAdja[tempo].append(i)
        
print("tabAdja Updated"+str(tabAdja), file=sys.stderr)


for i in range(e):
    ei = int(input())  # the index of a gateway node
    tabGateway.append(ei)
print("tabGateway "+str(tabGateway),file=sys.stderr)



# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print("node on which the Skynet agent is positioned this turn :"+str(si),file=sys.stderr)
    markedNode=[]
    currentNode = si
    queue=[]
    queue.append(si)
    oldNode=0
    while(currentNode not in tabGateway):
        currentNode=queue.pop(0)
        markedNode.append(currentNode)
        print("Current node : "+str(currentNode),file=sys.stderr)
        for i in range(0, len(tabAdja[currentNode])):
            tempo=tabAdja[currentNode][i]
            if(tempo not in markedNode and tempo not in queue):
                queue.append(tempo)
            print("Queue : "+str(queue),file=sys.stderr)
        #dirty but do while doest not exist in python    
        if(currentNode not in tabGateway):
            oldNode=currentNode
            print("OldNode : "+str(oldNode),file=sys.stderr)
    if(si in tabAdja[currentNode]):
        print(str(si)+" "+str(currentNode))
    else:
        print(str(oldNode)+" "+str(currentNode))

