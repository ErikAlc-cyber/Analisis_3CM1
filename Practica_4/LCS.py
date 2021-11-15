import time

#Bottom-up
def LCSBU(X, Y, cache):
    Aux = []
    for i in range(len(X)+1):
        for j in range(len(Y)+1):
            if (i == 0 or j == 0) :
                cache[i][j]=0
            elif (X[i-1] == Y[j-1]):
                cache[i][j] = cache[i - 1][j - 1] + 1
                Aux.append(X[i-1])
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    print("La cadena es:","".join(dict.fromkeys(Aux)))
    return cache[len(X)][len(Y)]

#Top-down
def LCSTD(X, Y, m, n):
    L = [[None]*(n + 1) for i in range(m + 1)]
    Aux = []
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                Aux.append(X[i-1])
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    print("La cadena es:","".join(dict.fromkeys(Aux)))
    return L[m][n]

def main():
    print("LCS programacion Dinamica")
    X = input("Dame el texto 1: ")
    Y = input("Dame el texto 2: ")
    m = len(X)
    n = len(Y)
    
    print("**********************")
    print("Aproximacion Top-Down")
    tic = time.perf_counter()
    print("El largo de la cadena es: ",LCSTD(X, Y, m, n))
    toc = time.perf_counter()
    print(f'Tiempo de ejecucion {(toc-tic):,.5f}')
    print("**********************")
    print("Aproximacion Bottom-Up")
    cache = [[-1 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]
    tic = time.perf_counter()
    print("El largo de la cadena es: ",LCSBU(X, Y, cache))
    toc = time.perf_counter()
    print(f'Tiempo de ejecucion {(toc-tic):,.5f}')
    print("**********************")
    
if __name__ == "__main__":
    main()