import random
from typing import Counter
import matplotlib.pyplot as plt
import numpy as np

def game(A, B,scorea,scoreb):
    a=random.randint(1, 7)
    b=random.randint(1, 7)
    if a>b:
        A+=100
        B-=100
        scorea+=1
        
    elif a<b:
        A-=100
        B+=100
        scoreb+=1
        
    else:
        pass
    return  A, B,scorea,scoreb 

def main():
    scorea=0
    scoreb=0
    A=10000
    B=1000000
    count=0
    while count <=1000:
        A,B,scorea,scoreb= game(A,B,scorea,scoreb)
        count+=1
    percenta=scorea/1000*100
    percentb=scoreb/1000*100
    print("percenta:{:.2f}%".format(percenta))
    print("percentb:{:.2f}%".format(percentb))

    # plt.figure(figsize=(10, 10), dpi=150)
    # plt.subplot(211)
    # plt.plot(np.arange(0, len(lista)),lista, 'k-')
    # plt.xlabel("times")
    # plt.ylabel("money")
    # plt.legend(["A"],loc=1)
    # plt.subplot(212)
    # plt.plot(np.arange(0, len(listb)), listb, 'r-')
    # plt.xlabel("times")
    # plt.ylabel("money")
    # plt.legend(["B"],loc=1)
    # plt.show()

if __name__ == "__main__":
    main()


