import sys
import math


#convert input to binary 
def iter_bin(s):
        sb = s.encode('ascii')
        return (format(b, '07b') for b in sb)

message = input()

ans=""
for s in iter_bin(message):
    ans+=s

# remove all spaces
ans =ans.replace(" ", "")

index=0
chuck=""

#fetch the binary array
while(index < len(ans)):
    currentChar = ans[index]
    
    nbOccu=1
    indexOccu=index+1
    
    #fetch while it finds the sama bit
    while(indexOccu <len(ans) and ans[indexOccu]==currentChar):
        nbOccu+=1
        indexOccu+=1
    if(currentChar=="0"):
        chuck+="00 "
    else:
        chuck+="0 "
    for i in range(0,nbOccu):
        chuck+="0"
    chuck+=" "
    index+=nbOccu
    
#remove leading and ending spaces
chuck=chuck.strip()
print(chuck)
        
            
            



