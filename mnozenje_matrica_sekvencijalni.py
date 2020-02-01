import numpy as np
A=np.array([[4,18,15],[16,45,30],[28,72,45]], dtype=np.int32)
B=np.array([[3,16,12],[12,40,24],[21,64,36]], dtype=np.int32)
C=np.matmul(A,B)
print("Produkt matrica iznosi: ", C)