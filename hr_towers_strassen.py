#https://www.hackerrank.com/contests/w10/challenges/towers/
from sys import exit
from math import ceil, log
height = long(raw_input())
diff_height = int(raw_input()) 
brick_heights = tuple(map(int,raw_input().split()))
MOD = 10**9 + 7

#Regular matrix muplication
def matMul(A,B):
    return [[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) % MOD for j in range(len(B[0]))] for i in range(len(A))]

#Make the matrix of dimensin NxN
def makeNxN(A):
    if len(A)<len(A[0]):
        A+=[[0]*len(A[0])]*abs(len(A)-len(A[0]))
    elif len(A)>len(A[0]):
        for i in range(len(A)):
            A[i].append(0)
    return A

#Make the matrix of dimesion 2^Nx2^N
def makePower2(A):
    A = makeNxN(A)
    if log(len(A),2)!= 0.0:
        for i in range((2**int(ceil(log(len(A[0]),2))) - len(A))):
            A.append([0]*len(A[0]))
    A = makeNxN(A)
    return A

#Adding two matrices
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

#Subtracting two matrices
def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

#Matrix muplication using Strassen algo
def strassen(A, B):
    n = len(A)
    if n <= 1:
        return matMul(A, B)
    else:
        halfSize = n/2
        a11 = [[0 for j in range(halfSize)] for i in range(halfSize)]
        A11 = [[0]*(halfSize)]*(halfSize)
        a12 = [[0 for j in range(halfSize)] for i in range(halfSize)]
        a21 = [[0 for j in range(halfSize)] for i in range(halfSize)]
        a22 = [[0 for j in range(halfSize)] for i in range(halfSize)]

        b11 = [[0 for j in range(halfSize)] for i in range(halfSize)]
        b12 = [[0 for j in range(halfSize)] for i in range(halfSize)]
        b21 = [[0 for j in range(halfSize)] for i in range(halfSize)]
        b22 = [[0 for j in range(halfSize)] for i in range(halfSize)]

        
        for i in range(halfSize):
            for j in range(halfSize):
                a11[i][j] = A[i][j]     
                a12[i][j] = A[i][j + halfSize]
                a21[i][j] = A[i + halfSize][j]
                a22[i][j] = A[i + halfSize][j + halfSize]

                b11[i][j] = B[i][j]           
                b12[i][j] = B[i][j + halfSize]   
                b21[i][j] = B[i + halfSize][j]    
                b22[i][j] = B[i + halfSize][j + halfSize]

        
        m1 = strassen(add(a11, a22), add(b11, b22))
        m2 = strassen(add(a21, a22), b11) 
        m3 = strassen(a11, subtract(b12, b22))
        m4 =strassen(a22, subtract(b21, b11))
        m5 = strassen(add(a11, a12), b22)
        m6 = strassen(subtract(a21, a11),add(b11, b12))
        m7 = strassen(subtract(a12, a22), add(b21, b22))

        
        c12 = add(m3, m5) 
        c21 = add(m2, m4) 
        c11 = subtract(add(add(m1, m4), m7), m5) 
        c22 = subtract(add(add(m1, m3), m6), m2) 

        
        C = [[0 for j in range(n)] for i in range(n)]
        for i in range(0, halfSize):
            for j in range(0, halfSize):
                C[i][j] = c11[i][j]
                C[i][j + halfSize] = c12[i][j]
                C[i + halfSize][j] = c21[i][j]
                C[i + halfSize][j + halfSize] = c22[i][j]
        return C

#Exponentiation by squaring
def matPow(A,n):
    #Padding matrix with 0 to make it of perfect dimesion of 2^n
    A = makePower2(A)
    Unity_Mat = [[1 if i==j else 0 for i in range(len(A))] for j in range(len(A))]
    while n:
        if n & 1:
            Unity_Mat = strassen(Unity_Mat,A)
        #Matricecs are multiplied using Strassen instead of regular muplication
        A = strassen(A,A)
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
x=[] #Transpose of F
for i in f[1:]:
    x.append([i])
x.append([0]) 
#Calculating last multiplication in regular way as 1 matrix is only 1 dimensional. So pedding it with 0 with increase the time  
R = matMul(M,x)
print (R[-2][0]*2) % MOD