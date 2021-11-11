import time
import math

def coefBin(n, k):
    if k == 1 or k == n:
        return 1
    elif k > n:
        return 0
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        div = a // (b*(n-k))
        return div

def binoCoeff(n, k):
    if k == 0 or k == n:
        return 1
    bin = binoCoeff(n-1, k-1) + binoCoeff(n-1, k)
    return bin

def pascal (n):
    list = [0] * n
    x = 0
    i = 0
    for i in range(n+1):
        j = x
        for j in range(0, -1, -1):
            if j == x or j == 0:
                list[j] = 1
            else:
                list[j] = list[j] + list[j-1]
        x = x + 1
    print("")
    triangle(list)
        
def triangle(list):
     
    
    k = len(list) - 1
    for i in range(0, len(list)):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        
        for j in range(0, i+1):
            print(list[j]," ", end="")
        print("\r")              

def main():
    print("**********************")
    n = int(input("Dame el valor de n:"))
    k = int(input("Dame el valor de k:"))
    print("")
    tic = time.perf_counter()
    c = binoCoeff(n, k)
    toc = time.perf_counter()
    print("El valor C(",n,",",k,") es ",c)
    print(f'Tiempo de ejecucion {(toc-tic):,.5f}')
    pascal (n)
    print("**********************")

if __name__ == "__main__":
    main()