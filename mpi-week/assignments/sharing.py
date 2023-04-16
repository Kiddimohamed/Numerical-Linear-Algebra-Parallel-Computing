 # write your program here
from mpi4py import MPI
TAILLE = comm.Get_size()
RANK = comm.Get_rank()
COMM = MPI.COMM_WORLD
while True:
    if RANK == 0:
        sendbuf = int("entrer un entier")
    else: 
        sendbuf = None    
    recvbuf = COMM.bcast(sendbuf, root = 0)    
    print('je suis le proc ',rank,"j'ai recu ",recvbuf)   
    if recvbuf < 0: break
