import numpy as np
def auxiliar(matriz_vector):
    try:
        column = len(matriz_vector[0])
        return column
    except TypeError:
        column = 1
        return column


def auxiliar_1(matriz_vector):
    try:
        column = len(matriz_vector[0])
        return True
    except TypeError:
        column = 1
        return False


def auxiliar_2(num_complex):
    real = num_complex.real
    imaginaria = -1 * num_complex.imag
    if imaginaria < 0:
        num = str(real) + str(imaginaria) + 'j'
    else:
        num = str(real) + '+' + str(imaginaria) + 'j'
    return complex(num)


def vectorSumaComplex(vector_1,vector_2):
    for i in range(len(vector_1)):
        vector_1[i] = vector_1[i] + vector_2[i]
    return vector_1


def vectorInverComplex(vector):
    for i in range(len(vector)):
        vector[i] = -1 * vector[i]
    return vector


def vectorMultEsComplex(vector, escalar):
    for i in range(len(vector)):
        vector[i] = escalar * vector[i]
    return vector

def matrizInverComplex(matriz):
    matriz = [[-1 * matriz[j][k] for k in range(len(matriz[0]))] for j in range(len(matriz))]
    return matriz


def matrizMultEsComplex(matriz, escalar):
    matriz = [[escalar * matriz[j][k] for k in range(len(matriz[0]))] for j in range(len(matriz))]
    return matriz


def trasMatrizVector (matriz_vector):
    rows = len(matriz_vector)
    column = auxiliar(matriz_vector)
    if auxiliar_1(matriz_vector):
        aux = [[matriz_vector[k][j] for k in range(rows)] for j in range(column)]
        aux = (aux[0] if len(aux) == 1 else aux)
    else:
        aux = [[matriz_vector[j] for k in range(column)] for j in range(rows)]
    return aux


def conjMatrizVector (matriz_vector):
    rows = len(matriz_vector)
    column = auxiliar(matriz_vector)
    if auxiliar_1(matriz_vector):
        for j in range(rows):
            for k in range(column):
                matriz_vector[j][k] = auxiliar_2(matriz_vector[j][k])
    else:
        for j in range(rows):
            matriz_vector[j] = auxiliar_2(matriz_vector[j])
    return matriz_vector[:]


def adjuntMatrizVector (matriz_vector):
    return trasMatrizVector(conjMatrizVector(matriz_vector))


def multMatrices (matriz_a, matriz_b):
    rows_a, rows_b, column_a, column_b = len(matriz_a), len(matriz_b), auxiliar(matriz_a), auxiliar(matriz_b)
    if rows_b == column_a:
        aux = [[0 for i in range(column_b)] for j in range(rows_a)]
        for h in range(column_b):
            for j in range(rows_a):
                for k in range(column_a):
                    aux[j][h] += matriz_a[j][k] * matriz_b[k][h]
        return aux
    else:
        return 'Las matrices no se pueden operar'


def dotProduct(vector_a,vector_b):
    size = len(vector_a)
    suma = 0
    for j in range(size):
        suma += vector_a[j] * vector_b[j]
    return suma


def normVector(vector):
    return (dotProduct(vector, vector))**(1/2)


def disVectors(vector_a, vector_b):
    a = np.array(vector_a)
    b = np.array(vector_b)
    vector = a - b
    return normVector(vector)

