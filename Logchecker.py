'''
DO NOT USE
Created on 26/03/2012

@author: ultrazoid_
'''
import os
import time

lalist = []
nn=0
dirs = os.listdir("/Logs")

for fil in dirs:
    print nn,":",fil
    lalist.insert(nn,fil)
    nn=nn+1

fn = raw_input("Please choose a log from the list:")
while fn != 'end':
    if fn in lalist:
        os.chdir("/Logs")
        print "File Found!"
        print "opening file"
        print "\n"
        time.sleep(3)
        ff = open(fn, 'r')
        fo = ff.read()
        print fo
        nn=0
    else:
        print "File not found!"
    for fil in dirs:
        print nn,":",fil
        lalist.insert(nn,fil)
        nn=nn+1
    fn = raw_input("Please choose a log from the list:")

