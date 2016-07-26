import sys
import math


#compute distance
def distance(longA,longB,latA,latB):
    y=(latB-latA)
    x=(longB-longA)*math.cos((latA+latB)/2)
    
    return math.sqrt(x*x+y*y)*6371
    
    
lon = float(input().replace(',','.'))
lat = float(input().replace(',','.'))
#print(lat)
n = int(input())


tabUtils=[]
for i in range(n):
    defib = input()
    l = defib.split(';')
    
    tabUtils.append(0)
    #Save useful information in tabUtils
    tabUtils[i]=(l[1],float(l[4].replace(',','.')),float(l[5].replace(',','.')))

#Initialize min distance
closerDefib=0
minDistance=distance(lon,tabUtils[0][1],lat,tabUtils[0][2])

#compute distance for each defib
for i in range(1,len(tabUtils)):
    currentDistance=distance(lon,tabUtils[i][1],lat,tabUtils[i][2])
    if(currentDistance < minDistance):
        closerDefib=i
        minDistance =currentDistance


print(tabUtils[closerDefib][0])


