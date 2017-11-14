# modules os.to help create directory and shutil to help copy files
import shutil
import os

#source directory and files directories
source = os.listdir("C:\Users\AllBlack\Desktop")
dest = ("C:\Users\AllBlack\Desktop\Music", "C:\Users\AllBlack\Desktop\Movies","C:\Users\AllBlack\Desktop\Files")

#creates directiory to copy files IN
os.mkdir(dest[0])
os.mkdir(dest[1])
os.mkdir(dest[2])

#conditions to help move files in to the right directory
for files in source:
    if files.endswith(".mp3"):
        shutil.move(files,dest[0])
    elif files.endswith(".mp4"):
        shutil.move(files,dest[1])
    elif files.endswith(".txt"):
    	shutil.move(files,dest[2])
    else:
	print "Done"

