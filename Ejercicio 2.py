A1 = [1,2,3,4,5]
A2 = [1,2,3,4,5]

def producto_arreglos(x,y):
    if len(x) == len(y):
        A3 = [x[i] * y[i]for i in range(len(x))]

        s = 0
        for x in A3:
            s += x
    return s


    
            
      
        

print(producto_arreglos(A1, A2))
