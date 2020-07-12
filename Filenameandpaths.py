import os

totalSize=0
parentPath = r'C:\Users\erich\Documents\Steinhart'


#Sum the size of the folder constituents
for filename in os.listdir(parentPath):

    filePath = os.path.join(parentPath,filename)
    if not os.path.isfile(filePath):
            continue
    else:
        totalSize = totalSize+os.path.getsize(filePath)

print(r'Total file size in the directory "'+parentPath+' is'+str(totalSize))

#make directory folders
#os.makedirs(r'C:\Users\erich\Desktop\Python\MakeDir\1\2\3')

#open files
helloFile = open(r'C:\Users\erich\Desktop\Python\MakeDir\openingTest.txt')
print(helloFile.read())
helloFile.close()


