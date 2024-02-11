# https://www.codewars.com/kata/5899a4b1a6648906fe000113/train/python

from collections import Counter


def find_routes(routes):
    output = []
    graph = {}
    for route in routes:
        graph[route[0]] = route[1]
    keys, values = set(graph.keys()), set(graph.values())

    def helper(route):
        output.append(route)
        if not route in graph:
            return
        return helper(graph[route])

    helper(list((keys - values))[0])  # Entry Key
    return ", ".join(output)


# Test Code
print(find_routes([["USA", "BRA"], ["JPN", "PHL"],
      ["BRA", "UAE"], ["UAE", "JPN"]]))
print(find_routes([('two', 'three'), ('one', 'two')]))
