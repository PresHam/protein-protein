import time
import threading
import random
import os

## This is the universe
print('Fiat Lux')
state = 1
board = {
    '0': [0, 0, 0, 0, 0, 0, 0, 0],
    '1': [0, 0, 0, 0, 0, 0, 0, 0],
    '2': [0, 0, 0, 0, 0, 0, 0, 0],
    '3': [0, 0, 0, 0, 0, 0, 0, 0],
    '4': [0, 0, 0, 0, 0, 0, 0, 0],
    '5': [0, 0, 0, 0, 0, 0, 0, 0],
    '6': [0, 0, 0, 0, 0, 0, 0, 0],
    '7': [0, 0, 0, 0, 0, 0, 0, 0]
}


def agent():
    value = 1
    x = 0
    y = 1
    while state == 1:
        if x == 8:
            x =
        if y == 8:
            y = 0
        free_will([x, y, value])
        x += 1
        y += 1
        time.sleep(3)


def free_will(position):
        x = str(position[0])
        y = position[1]
        value = position[2]
        board[x][y] = value


def visualize_universe():
    while state == 1:
        print('\n\n')
        for value in board.values():
            print(value)
        time.sleep(2)


def start_events(events):
    for value in events.values():
        value.start()


if __name__ == '__main__':
    print('We are here')
    time.sleep(2)
    events = {
        'reality': threading.Thread(target=visualize_universe),
        'humanity': threading.Thread(target=agent)
    }
    print('Events loaded, world about to begin')
    time.sleep(2)
    start_events(events)


