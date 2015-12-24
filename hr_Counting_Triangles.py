#https://www.hackerrank.com/contests/codestorm/challenges/ilia
import sys
from itertools import combinations

N = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
# your code goes here
tri = combinations(A,3)
ac = 0
ob = 0
rt = 0
for i in tri:
    if i[0]+i[1]>i[2] and i[1]+i[2]>i[0] and i[2]+i[0]>i[1]:
        temp = i[0]**2 + i[1]**2
        hype = i[2]**2
        if  temp > hype:
            ac += 1
        elif temp < hype:
            ob += 1
        else:
            rt += 1
print str(ac)+" "+str(rt)+" "+str(ob)
    
