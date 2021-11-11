import time

metrica = "from math import sqrt"

def fiboBotUp(n):
    if n<2 :
        return n
	
    else:  
        a = 0
        b = 1
        for x in range(n-1):
            temp = a + b
            a = b
            b = temp
    
    return b

def fiboTopDown(n, list):
    if n<2:
        return n
    elif list[n] != 0 :
        return list[n]
    list[n] = fiboTopDown(n-1, list) + fiboTopDown(n-2, list)
    return list[n]

def main():
    print("****************")
    
    print("Numeros de Fibonacci")
    num = int(input("Que numero deseas obtener?: "))
    list = []
    for _ in range(num+1):
        list.append(0)
    
    print("Enfoque Bottom-up")
    tic = time.perf_counter()
    temp1=fiboBotUp(num)
    toc = time.perf_counter()
    print("Resultado: ",temp1,"Tiempo: ",(toc-tic)," segundos")
    
    print("Enfoque Top-Down")
    tic = time.perf_counter()
    temp2=fiboTopDown(num, list)
    toc = time.perf_counter()
    print("Resultado: ",temp2,"Tiempo: ",(toc-tic)," segundos")

    print("******************")

if __name__ == "__main__":
    main()