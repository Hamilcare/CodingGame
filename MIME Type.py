import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
dico={}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dico[ext.lower()]=mt
    
#print(dico)
for i in range(q):
    fname = input()  # One file name per line.
    fname=fname.lower()
    #print(fname)
    
    if("."in fname):
        #last occurence of '.'
        indexExt = fname.rfind('.')
        #print(indexExt)
        #substring from'.' to the end
        extension=fname[indexExt+1:]
        #print(extension)
        
        if(extension in dico):
            print (dico[extension])
        else:
            print("UNKNOWN")
        
        
    else:
        print("UNKNOWN")


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

