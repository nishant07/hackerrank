#https://www.hackerrank.com/contests/epiccode/challenges/perfect-hiring
#First competitive program using Python. So you will find very poor python coding

def sstr(a):
    return a[a.find(" ")+1:a.find(" ",a.find(" ")+1)]
npx = raw_input()
aa = raw_input()
n = int(npx[:npx.find(" ")])
p = int(npx[npx.index(" ")+1:npx.rfind(" ")])
x = int(npx[npx.rfind(" ")+1:])
#print n
#print p
a = []
#a.append(int(aa[:aa.find(" ")]))
ts = aa
#s = sstr(aa)
#a.append(int(s))
for i in range(n/2-1):
    a.append(int(ts[:ts.find(" ")]))
    s = sstr(ts)
    a.append(int(s))
    ts = ts[ts.find(" ")+len(s)+2:]
#    print "i:",i
#print ts 
#print a    
if n%2 == 0:
    a.append(int(ts[:ts.find(" ")]))
    a.append(int(ts[ts.find(" ")+1:]))
else:
    a.append(int(ts[:ts.find(" ")]))
    a.append(int(ts[ts.index(" ")+1:ts.rfind(" ")]))
    a.append(int(ts[ts.rfind(" ")+1:]))   
#print a
mx = a[0]
f = 0
j = 0
for i in a:
    if mx < i*p:
        mx = i*p
        f = j
#    print "max:",mx,"-i*p:",i*p,"f:",f,"j:",j
    j = j + 1
    p = p - x
#print "f:",f+1,"j:",j
print f+1