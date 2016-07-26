import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
tab=[]
for i in range(n):
     tab.append(int(input()))
tab.sort()

mini=tab[1]-tab[0]

for i in range(1,len(tab)-1):
    tempo = tab[i+1]-tab[i]
    if(tempo<mini):
        mini = tempo
print(mini)
