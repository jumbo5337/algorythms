
start = "start"# 0
a = "a" # 1
b = "b"#  2
c = "c"#  3
d = "d"#  4
e = "e"#  5
f = "f"#  6
g = "g"#  7
h = "h"#  8
i = 'i'#  9
fin = "fin"# 10



infinity = float('inf')
graph = {}
graph[start] = {}
graph[start][a] = 10
graph[start][b] = 5
graph[start][c] = 6


graph[a] = {}
graph[a][e] = 7
graph[a][d] = 8

graph[b] = {}
graph[b][e] = 15
graph[b][d] = 9

graph[c] = {}
graph[c][g] = 25


graph[d] = {}
graph[d][h] = 6
graph[d][g] = 4

graph[e] = {}
graph[e][f] = 8
graph[e][h] = 6

graph[g] = {}
graph[g][i] = 2
graph[g][h] = 3

graph[f] = {}
graph[f][fin] = 3

graph[h] = {}
graph[h][fin] = 7

graph[i] = {}
graph[i][fin] = 2



graph[fin] = {}

costs = {}
costs[a] = 6
costs[b] = 2
costs[c] = infinity
costs[d] = infinity
costs[e] = infinity
costs[f] = infinity
costs[g] = infinity
costs[h] = infinity
costs[i] = infinity
costs[fin] = infinity

parents = {}
parents[a] = start
parents[b] = start
parents[c] = None
parents[d] = None
parents[e] = None
parents[f] = None
parents[g] = None
parents[h] = None
parents[i] = None
parents[fin] = None

processed = []
route = []

def find_fastest_path():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]

        for n in neighbours.keys():
            new_cost = cost + neighbours[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def display_route(node=None):
    # These vars could be passed into the function
    # if you wanted dynamic processing...

    start_node = start  # we look for this 'value'
    end_node = fin  # we look for this 'key'

    if node == start_node:  # we're done
        route.append(node)
        reverse_route = list(reversed(route))
        print('Fastest Route: ' + ' -> '.join(reverse_route))
    elif node is None:  # begin processing (this condition only passes once)
        end_parent = parents[end_node]  # get the parent node for the end node
        route.append(end_node)
        display_route(end_parent)
    else:
        parent = parents[node]
        route.append(node)
        display_route(parent)

find_fastest_path()
display_route()


