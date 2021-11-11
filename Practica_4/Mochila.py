def mochiDP(W, wt, val, n):
 
    if n == 0 or W == 0:
        return 0
    
    if (wt[n-1] > W):
        return mochiDP(W, wt, val, n-1)
 
    else:
        return max(
            val[n-1] + mochiDP(
                W-wt[n-1], wt, val, n-1),
            mochiDP(W, wt, val, n-1))


''' 
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
'''
 
def main():
    val = []
    wt = []
    test = 0
    
    
if __name__ == "__main__":
    main()