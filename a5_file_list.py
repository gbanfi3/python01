import os
import operator
import pprint

filenamesAllDict = {}
filenamesAllList = []

for dirname, dirnames, filenames in os.walk('/home/gbanfi3/alma'):

    # print path to all filenames.
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        filesize = os.stat(filepath).st_size
        filenamesAllList.append((filename, filesize, filepath))

        if filename in filenamesAllDict.keys():
            filenamesAllDict[filename] +=1
        else:
            filenamesAllDict[filename] = 1

sortedFilenamesAllList =sorted(filenamesAllDict.items(), key=operator.itemgetter(0))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(filenamesAllDict)
pp.pprint(filenamesAllList)
pp.pprint(sortedFilenamesAllList)

