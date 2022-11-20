# Quickly make list of file of certain format with this python code
# just enter file format and it will create txt file named {file-type}.txt



import os

reqft = input("Enter the type of files you want to list : ")

#abbreviations : 
    # reqft =  requested file type
    # reqfl  =  requsted file list 

reqfl  = []

allf = list(os.listdir())

for file in allf :
    if reqft in file :              #string matching
        reqfl.append(file) 

name  = reqft +' ' + 'list'
path = './{}'.format(name) +'.txt'

with open(path , 'w', encoding="utf-8") as f :
    i = 0
    while i < len(reqfl) :
        f.write(reqfl[i] + '\n')
        i += 1
