#https://www.hackerrank.com/contests/w10/challenges/towers/
from sys import exit
height = long(raw_input())
diff_height = int(raw_input()) 
brick_heights = tuple(map(int,raw_input().split()))
MOD = 10**9 + 7

#Matrix muplication in regular way
def matMul(A,B):
    return [[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) % MOD for j in range(len(B[0]))] for i in range(len(A))]

#Exponentiation by squaring
def matPow(A,n):
    Unity_Mat = [[1 if i==j else 0 for i in range(len(A))] for j in range(len(A))]
    A_copy = A
    while n:
        if n & 1:
            Unity_Mat = matMul(Unity_Mat,A)
        A = matMul(A,A)
        n //= 2
    return Unity_Mat

#List tells is a brick of certain height is available or not
height_exists = [0]*(min(height,15))
for i in range(1,min(height,15)+1):
    if i in brick_heights:
        height_exists[i-1] = 1

f = [0]*(min(height+1,16))
f[0] = 1
for i in range(1,min(height,15)+1):
    for j in range(0,i):
        f[i] += height_exists[j] * f[i-j-1]

if height<=15: #If height is less than 16 then no matrix multiplication is required
    print f[height]*2 % MOD
    exit()

M = [[1 if j == i+1 else 0 for j in range(min(height,15))] for i in range(min(height,15))]
height_exists.reverse()
M[-1] = height_exists
M = matPow(M,height-15)
x=[] #Transpose of M
for i in f[1:]:
    x.append([i])

#Calculating last multiplication in regular way as 1 matrix is only 1 dimensional. So pedding it with 0 with increase the time
R = matMul(M,x)
print (R[-1][0]*2) % MOD