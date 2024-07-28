#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import os


def load_json(file_path):
    if (os.path.exists(file_path) == False):
        return None
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def plot_graph(data, name):
    plt.plot(data['battle_won_mean_T'], data['test_battle_won_mean'])
    plt.xlabel('battle_won_mean_T')
    plt.ylabel('battle_won_mean')
    plt.title('Battle won mean')
    plt.savefig(name)
    plt.close()


if __name__ == '__main__':
    n = int(input("Please input the number of runs: "))
    path = '../pymarl/results/sacred/'
    graphName = 'pic/5m_vs_6m_'
    for i in range(1, n + 1):
        data = load_json(path + str(i) + '/info.json')
        if data is None:
            continue
        plot_graph(data, graphName + str(i) + '.png')