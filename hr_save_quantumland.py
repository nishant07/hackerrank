#https://www.hackerrank.com/contests/codestorm/challenges/save-quantumland
#!/bin/python

import sys
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    a = map(int,raw_input().strip().split(' '))
    c = a.count(1)
    i = 0
    while i < n-1:
        #print "a+"+str(i)+":"+str(a[i])
        #print i
        if a[i] == 0 and a[i+1] == 0:                
            a[i+1] = 1
            #print a
        i += 1
    print a.count(1) - c
