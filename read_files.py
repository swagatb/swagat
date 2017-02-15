import multiprocessing
import time
import multiprocessing
from multiprocessing import Pool
import time, sys, os

def follow(thejsonfile):
    thejsonfile.seek(0,2) 
    while True:
        line = thejsonfile.readline()
        print "new line = ",line
        if not line:
            time.sleep(1)
            continue
        print"at last", line


def jsonlog():
    try:
        logfile = open("a.txt","r")
    except IOError as e:
        logger.info("I/O error({0}): {1}".format(e.errno, e.strerror))

    return logfile

def main_loop(data):
    print "data = ",data


if __name__=="__main__":
    loglines = follow(jsonlog())
    #pool = multiprocessing.Pool(1)
    #pool.imap(main_loop, (loglines), 10)
    #pool.close()
    #pool.join()
