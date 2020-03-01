import numpy as np
from mpi4py import MPI
import time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
pocetak = time.time()
def f():
    return size
def test_funkcija():
    assert f()==size
    print("Test uspjesno prolazi.")
if rank==0:
    """Inicijalizacija matrica A, B i C"""
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.empty((size, size))
else:
    A = None
    B = np.empty((size, size))
    C = None
redak_A = np.empty(size)
comm.Scatter(A, redak_A, root=0)
comm.Bcast(B, root=0)
redak_C = np.empty(size)
for i in range(0, size):
    redak_C[i] = np.dot(redak_A, B.transpose()[i])
comm.Gather(redak_C, C, root=0)
if rank == 0:
    """Ispis produkta matrica A i B"""
    print("Produkt matrica iznosi: ", C)
kraj = time.time()
print("Trajanje izvodjenja koda: ", kraj-pocetak)
test_funkcija()