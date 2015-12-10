#height = long(raw_input())
height = long(8418749856060372)
#diff_height = int(raw_input()) 
diff_height = 14
#brick_heights = tuple(map(int,raw_input().split()))
brick_heights = (5,10,1,14,11,9,6,4,8,12,3,13,2,15)

mod = 10**9 + 7
towers_count = 0
height_exists = [0]*diff_height
for i in range(1,height):
	if i in brick_heights:
		height_exists[i-1] = 1 
#print height_exists		
#f = [0]*(height+1)
f[0] = 1
'''
for i in brick_heights:
	f[i] = 1
'''
for i in range(1,height+1):#min(height,15)+1):
	#print i
	for j in range(0,i):
		#print "fij",i,j,f[i]
		#print "height",height_exists[j]
		f[i] += height_exists[j] * f[i-j-1]
	#print "fi",f[i]
print f[height]*2 / mod