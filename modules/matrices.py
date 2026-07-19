def sumar_matrices(A, B):
    
    filas = len(A)

    columnas = len(A[0])

    resultado = []

    for i in range(filas):
        fila = []

        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        
        resultado.append(fila)
    
    return resultado