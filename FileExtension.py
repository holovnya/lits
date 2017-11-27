import glob

class FileExtension (object):
    extensionName = 'txt'
    extensionList = []
    
    def __init__(self, extensionName, extensionList):
        self.extensionName = extensionName
        self.extensionList = extensionList
    
    def printFileNames (self):
        for extension in self.extensionList:
            for file in glob.glob("*" + extension):
                print(file)
                
class FileExtensionList (FileExtension):
    fileList = []
    
    def __init__(self, objectList):
        for item in objectList:
            if isinstance(item, FileExtension):
                self.fileList.append(item)
            else:
                raise Exception('is not instance of FileExtension class')
        
    def printFileNameList (self, extensionList):       
        for extension in extensionList:
            for file in self.fileList:
                if file.extensionName == extension:
                    file.printFileNames()

fileList = []

with open('config.txt','r') as file:
    dictList = file.read().split(';')
    for item in dictList:
        dictPair = item.split(':')
        fileExten = FileExtension(item[0], item[1].split(','))
        fileList.append(fileExten)           
            
fileList = FileExtensionList(fileList) 

with open('extensionList.txt','r') as file:
    extenList = file.read().split(',')
    fileList.printFileNameList(extenList)