import random
import matplotlib.pyplot as plt
import numpy as np

def game(A, B, lista, listb):
    a=random.randint(1, 7)
    b=random.randint(1, 7)
    if a>b:
        A+=100
        B-=100
    elif a<b:
        A-=100
        B+=100
    else:
        pass
    lista.append(A)
    listb.append(B)
    return lista, listb, A, B

def main():
    lista=[]
    listb=[]
    A=10000
    B=1000000
    while A!=0 and B!=0:
        lista, listb, A, B = game(A,B,lista,listb)
    plt.figure(figsize=(10, 5), dpi=150)
    plt.subplot(211)
    plt.plot(np.arange(0, len(lista)), lista, 'k-')
    plt.legend(["A"])
    plt.subplot(212)
    plt.plot(np.arange(0, len(listb)), listb, 'r-')
    plt.legend(["B"])
    plt.show()

if __name__ == "__main__":
    main()


