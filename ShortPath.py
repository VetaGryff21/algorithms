# coding: utf-8
#

from typing import Dict, Tuple
from collections import deque

inf = float("inf")


class DijkstraAlgorythm:
    """ Реализация алгоритма Дейкстры """

    def __init__(
            self,
            graph: Dict[str, Dict[str, int]],
            parents: Dict[str, str],
            costs: Dict[str, float]
    ):

        # Граф
        self._graph = graph

        # Родители узлов
        self._parents = parents

        # Стоимости узлов
        self._costs = costs

        # Обработанные узлы
        self._processed = set()

    @property
    def costs(self) -> Dict[str, float]:
        return self._costs

    @property
    def parents(self) -> Dict[str, str]:
        return self._parents

    @property
    def graph(self) -> Dict[str, Dict[str, int]]:
        return self._graph

    def find_lower_cost_node(self) -> str:
        """ Находит узел с наименьшей стоимостью """

        lower_cost = inf
        lower_cost_node = None

        # Перебираем все узлы
        # print(self._processed)
        for node in self._costs:
            cost = self._costs[node]

            # Если этот узел с наименьшей стоимостью из уже виденных
            # и он ещё не был обработан
            if cost < lower_cost and node not in self._processed:
                lower_cost = cost
                lower_cost_node = node

        return lower_cost_node

    def find_lower_paths(self) -> None:
        """ Непосредственная реализация алгоритма """

        # Находим узел с наименьшей стоимостью
        node = self.find_lower_cost_node()
        print(node)
        input()

        # Пока не обработаны все узлы
        while node:
            cost = self._costs[node]
            neighbors = self._graph[node]

            # Перебрать всех соседей текущего узла
            for neighbor, neighbor_cost in neighbors.items():
                print("сосед: ", neighbor)
                # Считаем новую стоимость
                new_cost = cost + neighbor_cost

                # Если к соседу ближе добраться через текущий узел
                if new_cost < self._costs[neighbor]:
                    # Обновить стоимость для этого узла
                    self._costs[neighbor] = new_cost

                    # этот узел становится новым родителем для соседа
                    self._parents[neighbor] = node

            # Узел помечается как обработанный
            self._processed.add(node)

            # найти следующий узел для обработки и повторить цикл
            node = self.find_lower_cost_node()
            print(node)
            input()


def read_graph() -> Tuple[
    Dict[str, Dict[str, int]], Dict[str, str], Dict[str, float]
]:
    """
    Задание графа для алгоритма Дейкстры
    без проверок
    """
    n = int(input("Количество узлов: "))

    graph: Dict[str, Dict[str, int]] = {}  # сам граф
    for i in range(n):
        graph[str(i)] = {}
        raw_nodes = input(
            f"Узлы, в которые можно попасть из узла {i} (через пробел): "
        )
        nodes = raw_nodes.split()
        for node in nodes:
            cost = int(input(f"Стоимость до узла {node}: "))
            graph[str(i)][str(node)] = cost
    graph[str(n)] = {}

    # родители для каждого узла
    parents: Dict[str, str] = {
        node: min(graph)
        for node in graph[min(graph)]
    }

    # стоимости
    costs: Dict[str, float] = {}

    start = min(graph)
    for node in graph[start]:
        parents[node] = start
        costs[node] = graph[start][node]

    others = (key for key in graph if key not in parents)
    for node in others:
        costs[node] = inf
    del costs[start]

    print(graph)
    print(parents)
    print(costs)

    return graph, parents, costs


def print_readable_dijkstra_results(da: DijkstraAlgorythm):
    print("Кратчайший путь с первого до последнего узла: ")

    path = deque()
    node = max(da.parents)
    while node:
        path.insert(0, node)
        node = da.parents.get(node)
    print(" - ".join(path))

    common_cost = da.costs[max(da.parents)]
    print(f"Стоимость кратчайшего пути: {common_cost}")

    print()

    # print("Кратчайший путь до каждого узла: ")
    # print("Узел | Родитель")
    # for child, parent in da.parents.items():
    #     print(f"{child:>4} | {parent:>3}")
    #
    # print()

    print("Наименьшие пути до узлов:")
    for node, cost in da.costs.items():

        path = deque()
        find_node = node
        while find_node:
            path.insert(0, find_node)
            find_node = da.parents.get(find_node)

        print(f"{node:>2}: {cost:>3}\t(кратчайший путь: {' - '.join(path)})")