A1 = [1,2,3,4,5]
A2 = [1,2,3,4,5]

def producto_directo(v, w):
    if len(v) != len(w):
        return "Los arreglos deben tener la misma cantidad de numeros."
    
    producto = [v[i] * w[i] for i in range(len(v))]
    return producto

print(producto_directo(A1, A2))