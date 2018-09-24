#!/usr/bin/env python3

import os
import sys
import json

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'input', 'realms.json')) as f:
        realm_data = json.loads(f.read())

    realm_list = []
    realm_labels = {}
    for i, realm in enumerate(realm_data['realms']):
        realm_list.append(realm['slug'])
        realm_labels[i] = realm['name']

    adjacency_matrix = [[0 for x in range(len(realm_list))] for y in range(len(realm_list))]

    for realm in realm_data['realms']:
        for connected in realm['connected_realms']:
            adjacency_matrix[realm_list.index(realm['slug'])][realm_list.index(connected)] = 1

    rows, cols = np.where(np.array(adjacency_matrix) == 1)
    edges = zip(rows.tolist(), cols.tolist())
    graph = nx.Graph()
    graph.add_edges_from(edges)
    nx.draw(graph, node_size=50, labels=realm_labels, with_labels=True)
    plt.show()
