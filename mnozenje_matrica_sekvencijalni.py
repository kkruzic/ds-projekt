import numpy as np
import time
def f():
    return 3
def test_funkcija():
    assert f()==3
    print("Test uspjesno prolazi.")
pocetak = time.time()
"""Inicijalizacija matrica A i B"""
A=np.random.rand(3,3)
B=np.random.rand(3,3)
"""Produkt matrica A i B"""
C=np.matmul(A,B)
"""Ispis matrice C"""
print("Produkt matrica iznosi: ", C)
kraj = time.time()
print("Vrijeme izvodjenja: ", kraj-pocetak)
test_funkcija()