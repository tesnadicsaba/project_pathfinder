import matplotlib.pyplot as plt
import numpy as np


def show_map(board, path, style):
    surface = np.empty((250, 250), dtype=int)

    for i in range(250):
        for j in range(250):
            surface[i][j] = board.is_obs([i, j])

    fig, ax = plt.subplots(figsize=(14, 14))
    ax.imshow(surface, cmap=plt.cm.Dark2)

    if style == 1:
        ax.scatter(board.start[0], board.start[1], marker="*", color="yellow", s=25)
        ax.scatter(board.goal[0], board.goal[1], marker="*", color="red", s=25)

    if style == 2:

        for p in path:
            ax.scatter(p.x, p.y, marker=".", color="green", s=14)
            plt.plot(p.x, p.y)

        ax.scatter(board.start[0], board.start[1], marker="*", color="yellow", s=25)
        ax.scatter(board.goal[0], board.goal[1], marker="*", color="red", s=25)

    plt.show()
