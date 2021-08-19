import random
import matplotlib as plt
def game(A,B,lista,listb):
    a=random.randint(1,6)
    b=random.randint(1,6)
    if a>b:
        A+=100
        B-=100
    elif a<b:
        A-=100
        B+=100
    else:
        pass
    lista.append(a)
    listb.append(b)
    return lista,listb,A,B

def get_plot(lista,listb):
    plt.figure(figsize=(10, 5), dpi=150)
    plt.plot(len(lista),lista,marker = 'o',markersize = 1)
    plt.plot(len(listb),listb,marker = 'o',markersize = 1)
    plt.lengend(["A","B"])
    plt.show

def main():
    lista=[]
    listb=[]
    A=100
    B=200
    while A and B!=0:
        game(A,B,lista,listb)
    get_plot()
    
if __name__ == "__main__":
    main()


