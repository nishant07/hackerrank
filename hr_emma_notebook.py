#https://www.hackerrank.com/contests/codestorm/challenges/emmas-notebook
#!/bin/python

import sys


t = int(raw_input().strip())
# your code goes here
if t%2==0:
    s = (t/2+1)*(t/2+2)-1-(t/2+1)
    print s
else:
    s = ((t+1)/2)*((t+1)/2+1)-1
    print s