def MochiBr(W, wt, val, n):
 
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return MochiBr(W, wt, val, n-1)
 
    else:
        return max(
            val[n-1] + MochiBr(
                W-wt[n-1], wt, val, n-1),
            MochiBr(W, wt, val, n-1))
        
def MochiDBU(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

def MochiDTD(wt, val, W, n):
 
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
 
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + MochiDTD(
                wt, val, W-wt[n-1], n-1),
            MochiDTD(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = MochiDTD(wt, val, W, n-1)
        return t[n][W]

class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt
  
    def __lt__(self, other):
        return self.cost < other.cost
  
class FractionalKnapSack:
  
    """Time Complexity O(n log n)"""
    @staticmethod
    def getMaxValue(wt, val, capacity):
        """function to get maximum value """
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
  
        iVal.sort(reverse=True)
  
        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalValue
 
def main():
    val = []
    wt = []
    i = 0
    j = 0
    aux = 1
    n = int(input("Cuantos valores vas a agregar la lista? (#): "))
    
    while j < n:
        a = int (input("Que valor deseas agregar la lista de valores?:"))
        val.append(a)
        j+=1
    
    print("Lista de valores: ", val)
    
    while i < n:
        a = int (input("Que peso deseas agregar deseas agregar la lista?:"))
        wt.append(a)
        i+=1
    
    print("Lista de pesos: ", wt)
    
    while aux != 0:
        W = int(input("Cuanto es el maximo de peso a cargar?: "))
        global t 
        t = [[-1 for x in range(W + 1)] for y in range(n + 1)]
        
        print("*******************************")    
        print("Aproximacion Bruta")
        print("Valor maximo en la mochila:", MochiBr(W, wt, val, n))
        print("*******************************")
    
        print("Aproximacion Dinamica Bottom-up")
        print("Valor maximo en la mochila:", MochiDBU(W, wt, val, n))
        print("*******************************")
        
        print("Aproximacion Dinamica Top-Down")
        print("Valor maximo en la mochila:", MochiDTD(wt, val, W, n))
        print("*******************************")
    
        print("Aproximacion Greedy")
        maxValue = FractionalKnapSack.getMaxValue(wt, val, W)
        print("Valor maximo en la mochila:", maxValue)
        print("*******************************")
        
        W = 0
        
        aux = int(input("Quieres continuar? (S=1 / N=0): "))
        
    
if __name__ == "__main__":
    main()