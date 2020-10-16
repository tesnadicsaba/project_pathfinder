import math


class Point:
    x: int
    y: int
    z: float
    obs: int
    path_to: None
    # distance from start to finish
    step_dist: float

    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.z = 0
        self.obs = 0
        self.path_to = None
        self.step_dist = -1

    def clone(self, point):
        self.x = point.x
        self.y = point.y
        self.z = point.z
        self.obs = point
        self.path_to = None
        self.step_dist = point.step_dist

        return self

    def set_dist(self, value):
        self.step_dist = value

    def set_all(self, a, b, c, d):
        self.x = a
        self.y = b
        self.z = c
        self.obs = d
        self.path_to = None
        self.step_dist = -1

    def is_obs(self):
        return self.obs


# eucledian distance between 2 ponts in square
def eucledian_dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y) + (p1.z - p2.z) * (p1.z - p2.z))


class Grid:
    grid: [[Point(0, 0) for x in range(250)] for y in range(250)]
    start: [int, int]
    goal: [int, int]

    def __init__(self, start, goal, grid):

        self.grid = grid
        self.start = start
        self.goal = goal

    # value at position
    def val_at(self, position):
        return self.grid[position[0]][position[1]]

    def getSize(self):
        return [len(self.grid), len(self.grid[0])]

    def valid_position(self, position):
        size = self.getSize()
        return 0 <= position[0] < size[0] and 0 <= position[1] < size[1]

    def is_obs(self, position):
        return self.grid[position[0]][position[1]].obs

    def set_dist(self, nr_of_neighbours, max_dist=math.inf):
        board = self.grid

        for linee in range(250):
            for column in range(250):
                board[linee][column].step_dist = math.inf
                board[linee][column].path_to = None

        board[self.start[0]][self.start[1]].set_dist(0)
        if nr_of_neighbours == 8:
            neighbours = [[-1, -1], [-1, 1], [-1, 0], [1, -1], [1, 0], [1, 1], [0, -1], [0, 1]]
        else:
            neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        clist = [self.start]

        while clist:
            current = clist.pop(0)
            current_point = board[current[0]][current[1]]
            for neighbour in neighbours:
                nextt = [current[0] + neighbour[0], current[1] + neighbour[1]]
                if not self.valid_position(nextt):
                    continue

                next_point = board[nextt[0]][nextt[1]]

                if next_point.obs != 0:
                    continue

                if current_point.path_to is not None:
                    dist = eucledian_dist(current_point, next_point) + current_point.step_dist
                else:
                    dist = eucledian_dist(current_point, next_point)

                if dist > max_dist:
                    continue

                if next_point.step_dist > dist:
                    next_point.set_dist(dist)
                    next_point.path_to = current_point
                    clist.append(nextt)

        self.grid = board
        return self.grid

    def get_distance_to_goal(self):
        return self.grid[self.goal[0]][self.goal[1]].step_dist

    def find_path(self):
        path = []
        steps = 0
        current = self.grid[self.goal[0]][self.goal[1]]

        while current.path_to is not None:
            path.append(current)
            current = current.path_to
            steps += 1

        path.append(current)
        # steps += 1

        # print(f'steps to finish:', steps)
        return steps, path


