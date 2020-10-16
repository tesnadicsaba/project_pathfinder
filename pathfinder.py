from cls import *
from map import show_map
from animation import animate


def read_data_from_file(file):
    data_point = []
    grid = [[Point(0, 0) for x in range(250)] for y in range(250)]
    for line in file:
        for word in line.split():
            data_point.append(float(word))

        grid[int(data_point[0] - 263)][int(data_point[1] - 132)].set_all(int(data_point[0] - 263),
                                                                         int(data_point[1] - 132),
                                                                         data_point[2], int(data_point[3]))
        data_point.clear()
    return grid


def make_grid():
    file = open("surface.txt", "r")
    grid = read_data_from_file(file)

    return grid


class pathfinder:
    start: [int, int]
    finish: [int, int]
    show_animation = 0
    show_route = 0
    neighbours = 8
    steps = -1
    distance = -1
    path = []

    def __init__(self, start, finish, show_animation, show_route, neighbours):
        self.start = start
        self.finish = finish
        self.show_animation = show_animation
        self.show_route = show_route
        self.neighbours = neighbours
        self.myboard = Grid(self.start, self.finish, make_grid())
        self.steps, self.path = self.calc_dist()
        self.distance = self.myboard.get_distance_to_goal()

    def calc_dist(self):
        self.myboard.set_dist(self.neighbours, math.inf)
        return self.myboard.find_path()

    def show_dist_steps(self):
        if self.show_animation == 1:
            animate(self.myboard, self.path)

        return self.distance, self.steps

    def show_path(self):
        show_map(self.myboard, self.path, 2)
