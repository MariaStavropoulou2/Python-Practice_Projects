from disjoint_set import DisjointSet
import random
import time
import matplotlib.pyplot as plt
from collections import deque


class Maze:
    """The maze class.

    Generates a perfect maze of given length and height

    Attributes:
        entrance: An integer indicating the entrance of the maze.
        exit: An integer indicating the exit of the maze.
        length: The length of the maze
        height: The height of the maze
        size: length * height
        adjacency_list: Set of edges representing paths in maze
        adjacency_map: A dictionary representation of the edges (key: vertex, value: vertex neighbours)

    Methods:
        solver(s,e,option): Solve the maze with bfs and dfs algorithms
        visualize_maze(): Visualize maze with matplotlibs cmap
        evaluate_solution(solution): Evaluates to true or false a given sequence
    """

    # Constructor
    def __init__(
        self,
        length,
        height,
        entrance=None,
        entrance_direction=None,
        exit=None,
        exit_direction=None,
        seed=None,
    ):
        # If no seed is provided use current time
        if seed == None:
            random.seed(time.time())

        # Set length and height
        self._length = length
        self._height = height

        # If no entrance is provided default to node 1 and direction 'UP'
        if entrance == None or entrance_direction == None:
            self._entrance = 1
            self._entrance_direction = "UP"
        else:
            self._entrance = entrance
            self._entrance_direction = entrance_direction

        # If no exit is provided default to last node and direction 'RIGHT'
        if exit == None or exit_direction == None:
            self._exit = length * height
            self._exit_direction = "RIGHT"
        else:
            self._exit = exit
            self._exit_direction = exit_direction

        # Create all possible walls
        edges = list()
        for i in range(1, self.size + 1):
            if i % length > 0:
                edges.append((i, i + 1))
            if 1 + i // self.length < self.height:
                edges.append((i, i + self.length))

        # Do some suffling
        random.shuffle(edges)

        # Remove some walls
        removed = set()
        ds = DisjointSet()
        for i in range(1, self.size + 1):
            ds.find(i)
        for e1, e2 in edges:
            if ds.find(e1) != ds.find(e2):
                removed.add((e1, e2))
                ds.union(ds.find(e1), ds.find(e2))
                if ds.find(self._entrance) == ds.find(self._exit):
                    break
        self._adjacency_list = set(removed)

    # getter for entrance
    @property
    def entrance(self):
        return self._entrance

    # getter for exit
    @property
    def exit(self):
        return self._exit

    # getter for length
    @property
    def length(self):
        return self._length

    # getter for heigth
    @property
    def height(self):
        return self._height

    # getter for size
    @property
    def size(self):
        return self.height * self.length

    # getter for adjacency_list
    @property
    def adjacency_list(self):
        return self._adjacency_list

    # getter for adjacency_map
    @property
    def adjacency_map(self):
        adj_map = dict()
        for v1, v2 in self.adjacency_list:
            if v1 not in adj_map.keys():
                adj_map[v1] = set()
            adj_map[v1].add(v2)

            if v2 not in adj_map.keys():
                adj_map[v2] = set()
            adj_map[v2].add(v1)

        return adj_map

    # Solve the maze with bfs and dfs algorithms
    def solver(self, s, e, option):
        """Solve the maze"""
        frontier = deque()  # front search
        frontier.append(s)
        visited = set()  # visited nodes
        visited.add(s)
        prev = {s: None}  # for each node the previus one
        while frontier:  # while front search is not empty
            if option == "bfs" or option == "BFS":
                current_node = frontier.popleft()
            elif option == "dfs" or option == "DFS":
                current_node = frontier.pop()
            for next_node in self.adjacency_map[current_node]:
                if not next_node in visited:  # if next node isn't in visited nodes
                    frontier.append(next_node)
                    visited.add(next_node)
                    prev[next_node] = current_node

        # create the path from e to s
        path = []
        at = e
        while at != None:
            path.append(at)
            at = prev[at]

        # reverse the path to create the final path that we want
        path = path[::-1]

        # if s and e are connected return path
        if path[0] == s:
            return path

        # else return an empty list
        return []

    def visualize_maze(self):
        """Visualize maze with matplotlibs cmap"""
        grid = [[1 for _ in range(3 * self._length)] for _ in range(3 * self._height)]

        for point, direction in [
            (self._entrance, self._entrance_direction),
            (self._exit, self._exit_direction),
        ]:
            point_x = ((point - 1) % self._length) * 3 + 1
            point_y = ((point - 1) // self._length) * 3 + 1

            grid[point_y][point_x] = 0
            if direction == "UP":
                grid[point_y - 1][point_x] = 0
            elif direction == "RIGHT":
                grid[point_y][point_x + 1] = 0
            elif direction == "DOWN":
                grid[point_y + 1][point_x] = 0
            elif direction == "LEFT":
                grid[point_y][point_x - 1] = 0

        for e1, e2 in self._adjacency_list:
            if e1 > e2:
                e1, e2 = e2, e1

            point_x = ((e2 - 1) % self._length) * 3 + 1
            point_y = ((e2 - 1) // self._length) * 3 + 1
            grid[point_y][point_x] = 0

            point_x = ((e1 - 1) % self._length) * 3 + 1
            point_y = ((e1 - 1) // self._length) * 3 + 1
            grid[point_y][point_x] = 0

            if (e1 - 1) // self._length == (e2 - 1) // self._length:
                grid[point_y][point_x + 1] = 0
                grid[point_y][point_x + 2] = 0
            else:
                grid[point_y + 1][point_x] = 0
                grid[point_y + 2][point_x] = 0

        plt.figure(figsize=(10, 10))
        plt.imshow(grid, cmap=plt.cm.binary, interpolation="nearest")
        plt.xticks([]), plt.yticks([])
        plt.show()

    def evaluate_solution(self, solution):
        """Evaluates to true or false a given sequence"""
        if solution[0] != self.entrance or solution[-1] != self.exit:
            return False
        if len(solution) != len(set(solution)):
            return False
        for i in range(1, len(solution)):
            if (solution[i], solution[i - 1]) not in self.adjacency_list and (
                solution[i - 1],
                solution[i],
            ) not in self.adjacency_list:
                return False
        return True


def main():
    length = int(input("Give length for the maze: "))
    height = int(input("Give height for the maze: "))
    en_ex = input(
        "Do you want to choose the entrance and exit for the maze?(Please answer with Yes or No) "
    )
    if (
        en_ex == "Yes"
        or en_ex == "YES"
        or en_ex == "yes"
        or en_ex == "Y"
        or en_ex == "y"
    ):

        entrance = int(input("Give the start num position for the maze: "))
        entrance_direction = input("Give the start position for the maze: ")
        exit = int(input("Give the end num position for the maze: "))
        exit_direction = input("Give the end position for the maze: ")
        m1 = Maze(
            length=length,
            height=height,
            entrance=entrance,
            entrance_direction=entrance_direction,
            exit=exit,
            exit_direction=exit_direction,
        )
    else:
        m1 = Maze(length=length, height=height)
    option = input("How do you want to solve the maze? (with bfs or dfs algorithm) ")

    m1.visualize_maze()
    print(m1.evaluate_solution(m1.solver(m1.entrance, m1.exit, option)))


if __name__ == "__main__":
    main()
