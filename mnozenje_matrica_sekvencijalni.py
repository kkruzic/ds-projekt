import numpy as np
"""Inicijalizacija matrica A i B"""
A=np.random.rand(3,3)
B=np.random.rand(3,3)
"""Produkt matrica A i B"""
C=np.matmul(A,B)
"""Ispis matrice C"""
print("Produkt matrica iznosi: ", C)