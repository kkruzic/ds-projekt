import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank==0:
    A = np.array([[4, 18, 15], [16, 45, 30], [28, 72, 45]], dtype=np.int32)
    B = np.array([[3, 16, 12], [12, 40, 24], [21, 64, 36]], dtype=np.int32)
    C = np.empty(dtype=np.int32, shape=(3,3))
else:
    A = None
    B = None
    C = None
redak_A = np.empty(3, dtype=np.int32)
redak_B = np.empty(3, dtype=np.int32)
comm.Scatter(A, redak_A, root=0)
comm.Scatter(B, redak_B, root=0)
element_C = np.dot(redak_A, redak_B)
comm.Gather(element_C, C, root=0)
if rank == 0:
    print("Produkt matrica iznosi: ", C)