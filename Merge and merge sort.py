#EE-174
import time
import matplotlib.pyplot as plt
def MergeSort(A): 
    n=len(A) 
    s=list( ) 
    if n==1: 
        s=A 
    else: 
        a=(n//2) 
        s1=MergeSort(A[0:a]) 
        s2=MergeSort(A[a:n]) 
        s=merge(s1,s2) 
    return s
def merge(A,B): 
    n1=len(A) 
    n2=len(B) 
    A=A+[float('inf')] 
    B=B+[float('inf')] 
    i=0 
    j=0 
    M=list( ) 
    for k in range(0,n1+n2): 
        if A[i]<=B[j]: 
            M=M+[A[i]] 
            i=i+1 
        else: 
            M=M+[B[j]] 
            j=j+1 
    return M 
C= MergeSort([21,11,5])
D= MergeSort([4,3,2])
E= merge(C, D)
