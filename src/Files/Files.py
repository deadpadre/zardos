'''
Created on 10.03.2013

@author: deadpadre
'''

def isAlpha(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        return True
    else:
        return False

def makeDictionary(srcfile):
    sfile = open(srcfile, 'r');
    lines = sfile.readlines()
    sfile.close();
    
    rdictionary = []
    for i in xrange(len(lines)):
        if (len(lines[i].split()) != 0 and lines[i][0] != '/'):
            rdictionary.append(lines[i].split())
    
    dictionary = []
    for i in xrange(len(rdictionary)):
        dictionary.append([])
        for j in xrange(len(rdictionary[i])):
            if not isAlpha(rdictionary[i][j][0]):
                dictionary[i].append(' '.join(rdictionary[i][:j]))
                dictionary[i].append(' '.join(rdictionary[i][j:]))
                break
            if j == len(rdictionary[i]) - 1:
                print 'ERROR LE FATALE AT LINE %d IN AFTERFILE' % i
                exit(0)
    return dictionary