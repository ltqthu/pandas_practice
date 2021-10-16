import random
import matplotlib.pyplot as plt
import numpy as np


def dice_game_process(A, B):
    list_a, list_b = [], []
    while True:
        a = random.randint(1, 7)
        b = random.randint(1, 7)
        if a > b:
            A += 100
            B -= 100
        elif a < b:
            A -= 100
            B += 100
        else:
            pass
        list_a.append(A)
        list_b.append(B)
        if A <= 0 or B <= 0:
            break
    return list_a, list_b


def dice_game_judge(A, B):
    while True:
        a = random.randint(1, 7)
        b = random.randint(1, 7)
        if a > b:
            A += 100
            B -= 100
        elif a < b:
            A -= 100
            B += 100
        else:
            pass
        if A <= 0 or B <= 0:
            break
    return 0 if A > 0 else 1

# 游戏一直玩下去，直到对方破产游戏才算赢，统计A和B的胜率
def dice_game_statistic(A, B, max_times):
    win_times_a, win_times_b = 0, 0
    for i in range(max_times):
        if dice_game_judge(A, B) == 0:
            win_times_a += 1
        else:
            win_times_b += 1
    return win_times_a/max_times, win_times_b/max_times

def plot_single(A, B):
    list_a, list_b = dice_game_process(A, B)
    plt.figure(figsize=(10, 10), dpi=150)
    plt.subplot(211)
    plt.plot(np.arange(0, len(list_a)),list_a, 'k-')
    plt.xlabel("times")
    plt.ylabel("money")
    plt.legend(["A"],loc=1)
    plt.subplot(212)
    plt.plot(np.arange(0, len(list_b)), list_b, 'r-')
    plt.xlabel("times")
    plt.ylabel("money")
    plt.legend(["B"], loc=1)
    plt.show()


if __name__ == "__main__":
    A, B = 10000, 1000000
    max_times = 100
    # plot_single(A, B)
    print(dice_game_statistic(A, B, max_times))


