import numpy as np
import pylab as plt


def get_data(board):
    surface = np.empty((250, 250))
    for i in range(board.getSize()[0]):
        for j in range(board.getSize()[1]):
            surface[i][j] = int(board.is_obs([i, j]))

    return surface


def animate(board, path):
    path = reversed(path)

    # for the first frame generate the plot
    surface = get_data(board)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.imshow(surface, cmap=plt.cm.Dark2)
    ax.scatter(board.start[0], board.start[1], marker="*", color="yellow", s=25)
    ax.scatter(board.goal[0], board.goal[1], marker="*", color="red", s=25)

    # ... for subsequent times only update the data
    for p in path:
        surface[p.x][p.y] = 3

        ax.scatter(p.x, p.y, marker=".", color="green", s=14)
        plt.draw()
        plt.pause(0.05)
    # plt.pause(5)
    # plt.savefig('fig.png')
