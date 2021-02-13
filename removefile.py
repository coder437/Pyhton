import os
import shutil
path = input("enter the name of the folder to be sorted")
list_of_files = os.listdir(path)
for f in list_of_files:
    name,ext = os.path.splitext(f)
    ext = ext[1:]
    if ext=='':
        continue

    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+f,path+"/"+ext+"/"+f)
    else :
        os.makedirs(path+'/'+ext)
        shutil.move(path+"/"+f,path+"/"+ext+"/"+f)

    
