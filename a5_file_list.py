import os
import operator
from operator import itemgetter
import pprint
pp = pprint.PrettyPrinter(indent=4)


#dirr = '/home/gbanfi3/alma'
#dirr = '/media/gbanfi3/WD2T/tanulás/logika/'
#dirr = '/media/gbanfi3/WD2T/tanulás/IT/'
dirr = '/media/gbanfi3/WD2T/tanulás/draw/'
filesizeLimit = 100000

filenamesAllDict = {}
filenamesAllList = []

for dirname, dirnames, filenames in os.walk(dirr):

    # print path to all filenames.
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        filesize = os.stat(filepath).st_size
        filenamesAllList.append((filename, filesize, filepath))

        if filesize < filesizeLimit:
            continue

        #kulcs = filename + "xxx" + str(filesize)
        kulcs = filename
        if filename in filenamesAllDict.keys():
            filenamesAllDict[kulcs] +=1
        else:
            filenamesAllDict[kulcs] = 1

#pp.pprint(filenamesAllDict)
#pp.pprint(filenamesAllList)

#sortedFilenamesAllList =sorted(filenamesAllDict.items(), key=operator.itemgetter(0))
#pp.pprint(sortedFilenamesAllList)

sortedFilenamesAllList = list(filenamesAllDict.items())
sortedFilenamesAllList.sort(key=itemgetter(1))
pp.pprint(sortedFilenamesAllList)



