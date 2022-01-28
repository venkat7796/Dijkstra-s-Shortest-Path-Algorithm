# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import heapq


def dijkstra(gr, st, en):
    """
    HashMap to maintain cost and predecessors for each Node
    Initially the value will be set to infinity and predecessor list will be empty
    """
    node_det = {
        "A": {"cost": float("inf"), "pre": []},
        "B": {"cost": float("inf"), "pre": []},
        "C": {"cost": float("inf"), "pre": []},
        "D": {"cost": float("inf"), "pre": []},
        "E": {"cost": float("inf"), "pre": []}
    }
    # The Cost for starting node will always be 0
    node_det[st]["cost"] = 0
    # List to store visited nodes
    visited = []
    temp = st
    # Loop according to the length of the graph
    for i in range(len(gr)):
        # Min Heap to determine the next neighbour to be used for iteration
        min_heap = []
        if temp not in visited:
            visited.append(temp)
            # Iterate through all the neighbours of the node
            for j in gr[temp]:
                if j not in visited:
                    # Determine the cost required to reach the node
                    temp_cost = node_det[temp]["cost"] + gr[temp][j]
                    # If that cost is less than the existing it means it is the shortest path
                    if temp_cost < node_det[j]["cost"]:
                        node_det[j]["cost"] = temp_cost
                        node_det[j]["pre"] = node_det[temp]["pre"] + list(temp)
                    # Push it to the heap to determine the neighbour with minimum cost i.e. the shortest path
                    heapq.heappush(min_heap, [node_det[j]["cost"], j])
            # Heapify to determine the next neighbour
            if min_heap:
                heapq.heapify(min_heap)
                temp = min_heap[0][1]
    # Print the shortest path and the shortest neighbour
    print("The shortest distance from", st, "to", en, "is", node_det[en]["cost"])
    print("The shortest path is", node_det[en]["pre"] + list(en))


# Press the green button in the gutter to run the script.
graph = {
        "A": {"B": 6, "D": 1},
        "B": {"C": 5},
        "C": {},
        "D": {"E": 1, "B": 2},
        "E": {"C": 5}
}
start = "A"
destination = "C"

dijkstra(graph, start, destination)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
