import unittest
import numpy as np
from random import randint
import VectorComplexLibrary as vcl

TESTS = 10
SEED = 1e2
SEED_2 = 10

def conv(dupla):
    return complex(str(dupla[0]) + ('+' if dupla[1] >= 0 else '') + (str(dupla[1])) + 'j')

class testfunciones(unittest.TestCase):

    def test_suma_vector(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            vector_a = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_b = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_a_np = np.array(vector_a[:])
            vector_b_np = np.array(vector_b[:])
            self.assertTrue((vcl.vectorSumaComplex(vector_a[:], vector_b[:]) == vector_a_np + vector_b_np).all())

    def test_inver_vector(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            vector_a = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_a_np = np.array(vector_a[:])
            self.assertTrue((vcl.vectorInverComplex(vector_a[:]) == -1 * vector_a_np).all())

    def test_escalar_vector(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            escalar = conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED))))
            vector_a = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_a_np = np.array(vector_a[:])
            self.assertTrue((vcl.vectorMultEsComplex(vector_a[:], escalar) == escalar * vector_a_np).all())

    def test_suma_matriz(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_b = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            matriz_b_np = np.array(matriz_b[:])
            self.assertTrue((vcl.matrizSumaComplex(matriz_a[:], matriz_b[:]) == matriz_a_np + matriz_b_np).all())

    def test_inver_matriz(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            self.assertTrue((vcl.matrizInverComplex(matriz_a[:]) == -1 * matriz_a_np).all())

    def test_escalar_matriz(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            escalar = conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED))))
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            self.assertTrue((vcl.matrizMultEsComplex(matriz_a[:], escalar) == escalar * matriz_a_np).all())

    def test_trasponer_matriz(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            self.assertTrue((vcl.trasMatrizVector(matriz_a[:]) == np.transpose(matriz_a_np)).all())

    def test_conjugar_matriz(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            self.assertTrue((vcl.conjMatrizVector(matriz_a[:]) == np.conj(matriz_a_np)).all())

    def test_adjunta_matriz(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            self.assertTrue((vcl.adjuntMatrizVector(matriz_a[:]) == np.transpose(np.conj(matriz_a_np))).all())

    def test_multi_matriz(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(columns)]
                        for k in range(rows)]
            matriz_b = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            matriz_b_np = np.array(matriz_b[:])
            self.assertTrue((vcl.multMatrices(matriz_a[:], matriz_b[:]) == np.dot(matriz_a_np, matriz_b_np)).all())

    def test_accion(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(columns)]
                        for k in range(rows)]
            vector = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(columns)]
            self.assertTrue((vcl.accion(matriz_a[:], vector) == np.dot(matriz_a, vector)).all())

    def test_producto_interno(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            vector_a = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_b = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_a_np = np.array(vector_a[:])
            vector_b_np = np.array(vector_b[:])
            self.assertTrue((vcl.dotProduct(vector_a[:], vector_b[:]) == np.inner(np.conj(vector_a_np), vector_b_np)).
                            all())

    def test_norma_vector(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            vector_a = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_a_np = np.array(vector_a[:])
            self.assertTrue((vcl.normVector(vector_a[:]) == (np.inner(np.conj(vector_a_np), vector_a_np))**(1/2)).all())

    def test_distancia(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            vector_a = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_b = [conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
            vector_c = np.array(vector_a[:]) - np.array(vector_b[:])
            self.assertTrue((vcl.disVectors(vector_a[:], vector_b[:]) == (np.inner(np.conj(vector_c), vector_c))**(1/2))
                            .all())

    def test_hermitian(self):
        for i in range(TESTS):
            valor = None
            size = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(size)]
                        for k in range(size)]
            matriz_a_np = np.conj(np.transpose(np.array(matriz_a)))
            if (matriz_a_np == matriz_a).all():
                valor = True
            else:
                valor = False
            self.assertTrue(vcl.matrizHermitian(matriz_a) == valor)

    def test_unitary(self):
        for i in range(TESTS):
            valor = None
            size = randint(2, SEED_2)
            aux = [[(1 if j == k else 0) for k in range(size)]for j in range(size)]
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(size)]
                        for k in range(size)]
            matriz_a_np = np.dot(np.conj(np.transpose(np.array(matriz_a))), matriz_a)
            if (matriz_a_np == aux).all():
                valor = True
            else:
                valor = False
            self.assertTrue(vcl.matrizUnitary(matriz_a) == valor)

    def test_tensor_product(self):
        for i in range(TESTS):
            rows = randint(2, SEED_2)
            columns = randint(2, SEED_2)
            matriz_a = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(columns)]
                        for k in range(rows)]
            matriz_b = [[conv((randint(-int(SEED), int(SEED)), randint(-int(SEED), int(SEED)))) for j in range(rows)]
                        for k in range(columns)]
            matriz_a_np = np.array(matriz_a[:])
            matriz_b_np = np.array(matriz_b[:])
            self.assertTrue((vcl.tensorProduct(matriz_a[:], matriz_b[:]) == np.tensordot(matriz_a_np, matriz_b_np, axes=0)).all())

if __name__ == '__main__':
    unittest.main()