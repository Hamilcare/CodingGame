import sys
import math
 

 
#Largeur d'un caractère
l = int(input())
#Hauteur d'un caractère
h = int(input())
 
#Chaine que l'on veut écrire
t = input()
 
#Contient le tableau 2D ASCII art
s=[]
for i in range(h):
    row = input()
    tempo=[]
    for j in range(len(row)):
        tempo.append(row[j])
    s.append(tempo)
 
 
#Contient la réponse
ans=""
t=t.upper()
#print(t)
for index in range(h):
    for i in range(len(t)):
        asciiValue = ord(t[i])
        #Si caractère spécial
        if(asciiValue <65 or asciiValue>90):
            asciiValue = ord('@')
           
        start = (asciiValue-65)*l
        for j in range (start,start +l):
          #  print(i)
            ans+=s[index][j]
       
    ans+="\n"
print(ans)
