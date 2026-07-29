import os
from fileinput import filename


class FileHandling:
    def __init__(self,f_name):
        self.filename=f_name

    def read_file(self):
       # x = open(self.filename,"r")
       # with command takes care of closing file after wards
       #with open(self.filename) as x:
       with open(self.filename,"a") as x:
           x.write("XTZ")
        #print(x.read())
       #os.remove("FilePath")   --- This will delete the file.
       # to check if file exists: os.path.exists("filePath") --- returns bool.
       # os.rmdir("") --to remove a directory