import urllib.request
import time
import collections
import re

#download files
urlList = ["http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-macbeth-46.txt","http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-twelfth-20.txt","http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-hamlet-25.txt","http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-othello-47.txt","http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-coriolanus-24.txt"]

fileNameList = []

startTimeDownloadFiles = time.time()

for url in urlList:
    fileName = url[url.index('-') + 1 : url.index('-',url.index('-') + 1)]
    fileNameList.append(fileName)
    urllib.request.urlretrieve (url,fileName + '.txt')

#creation of main file
generalfile = open('generalFile.txt', 'w')

generalfile.write('William Shakespeare' + '\n')

for name in  fileNameList:
    file = open(name + '.txt', 'r')
    generalfile.write(name + '\n' + file.read() + '\n')
    file.close()

generalfile.close()

endTimeDownloadFiles = time.time() - startTimeDownloadFiles

#split file into words
listOfWords = []

with open('generalFile.txt','r') as generalfile:
    for line in generalfile:
        for word in line.split():
            if len(re.sub('[^a-z0-9]', '', word.lower())) > 4:
                listOfWords.append(re.sub('[^a-z0-9]', '', word.lower()))
                

#get top 1000 words and insert them into new file  
startTimeGetTopWords = time.time()

topWords = collections.Counter(listOfWords).most_common(1000)

with open('author_most_using_words.txt','w') as finalFile:
    for topWord in topWords:
        finalFile.write(topWord[0] + ' - ' + str(topWord[1]) + '\n')
        
endTimeGetTopWords = time.time() - startTimeGetTopWords

print('Time to download files and create new common file - ' + str(endTimeDownloadFiles))

print('Time to calculate top 1000 top words and create new file with them - ' + str(endTimeGetTopWords))