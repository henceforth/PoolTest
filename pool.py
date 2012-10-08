#!/bin/python2.7

import multiprocessing as mp
import time
import binascii
import hashlib

def run(startEnd):
    start, end = startEnd
    print "current process id: %i, start %i, end %i" % (mp.current_process().pid, start, end)
    numbers = range(start, end)
    return getMd5(numbers)
    
def getMd5(stringArray):
    returnArray = []
    for n in stringArray:
        returnArray.append("%s - %s" % (n, binascii.b2a_hqx(hashlib.md5(str(n)).digest())))

    return returnArray

if __name__=="__main__":
    p1 = mp.Pool()
    #eine million integer pro kern
    argArray = [(0, 1000000), (1000000, 2000000), (2000000, 3000000), (3000000, 4000000)]
    file = open("hashes.log", "w")
    for n in p1.map(run, argArray):
        for m in n:
            file.write(m+'\n')
            #print m

    #result = p1.apply_async(run, argArray) 
    #p1.close()
    #p1.join()
    #print pool.map(run, argArray)


