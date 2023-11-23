"""
Instruction:
https://docs.google.com/document/d/10bKX8rk00bkDO2u7kknagpn075-onj6bEbFku7WpHTo/edit#heading=h.c3dqsmniumt
"""

import random

def roboBuddy1():
    currentx = 0
    currenty = 0
    while True:
        direction = input("Enter direction (up, down, left, right): ")
        if direction == "up" and currenty < 2:
            currenty += 1
        elif direction == "down" and currenty > -2:
            currenty -= 1
        elif direction == "left" and currentx > -2:
            currentx -= 1
        elif direction == "right" and currentx < 2:
            currentx += 1
        else:
            print("Robot can't move further in that direction.")

def roboBuddy2(n):
    x = 0
    y = 0
    while True:
        direction = input("Enter direction (up, down, left, right): ")
        if direction == "up" and y < (n-1)/2:
            y += 1
        elif direction == "down" and y > -(n-1)/2:
            y -= 1
        elif direction == "left" and x > -(n-1)/2:
            x -= 1
        elif direction == "right" and x < (n-1)/2:
            x += 1
        else:
            print("Robot can't move further in that direction.")

def roboBuddy3(n):
    x = 0
    y = 0
    steps = 10000
    directions = ['up', 'down', 'left', 'right']
    movements = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
    for i in range(steps):
        direction = random.choice(directions)
        if direction == "up" and y < (n-1)/2:
            y += 1
        elif direction == "down" and y > -(n-1)/2:
            y -= 1
        elif direction == "left" and x > -(n-1)/2:
            x -= 1
        elif direction == "right" and x < (n-1)/2:
            x += 1
        movements[direction] += 1
    print("Final position: ({}, {})".format(x, y))
    for direction, count in movements.items():
        print("{} steps {}: {}".format(count, direction, count))

def roboBuddy4(n):
    x = (n-1)//2
    y = (n-1)//2
    steps = 100000
    directions = ['up', 'down', 'left', 'right']
    movements = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
    room = [['wall' for j in range(n)] for i in range(n)]
    exit_x, exit_y = random.choice(range(n)), random.choice(range(n))
    room[exit_x][exit_y] = 'exit'
    for i in range(steps):
        direction = random.choice(directions)
        if direction == "up" and y > 0:
            y -= 1
        elif direction == "down" and y < n-1:
            y += 1
        elif direction == "left" and x > 0:
            x -= 1
        elif direction == "right" and x < n-1:
            x += 1
        movements[direction] += 1
        if room[x][y] == 'exit':
            print("RoboBuddy found the exit!")
            break
    else:
        print("RoboBuddy couldn't find the exit after 100,000 steps.")
    print("Final position: ({}, {})".format(x, y))
    for direction, count in movements.items():
        print("{} steps {}: {}".format(count, direction, count))
    print("Exit is located at: ({}, {})".format(exit_x, exit_y))
    
roboBuddy4(10000)
