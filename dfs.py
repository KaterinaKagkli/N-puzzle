import random
import copy
import sys
import math


def main():
    initial_state = creating_initial_state()
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, None]]         # Setting puzzle goal
    frontier = []
    frontier.insert(0, initial_state)
    close_set = []

    # Starting solution with the initial state as first iteration
    begin_solution(frontier, goal, close_set)


def begin_solution(frontier, goal, close_set):
    set_current_state(frontier, goal, close_set)


def set_current_state(frontier, goal, close_set):
    new_current_state = frontier[0]
    print_array(new_current_state)
    # If current state exists in closed set skip to the next in the frontier
    if new_current_state in close_set:
        children = []
        set_frontier(frontier, children, goal, close_set)

    if new_current_state == goal:
        close_set = set_closed_set(frontier[0], close_set)
        print("Solution found")
        for i in close_set:
            print_array(i)
            sys.exit()
    find_children(frontier, new_current_state, goal, close_set)


def set_frontier(frontier, children, goal, close_set):
    # Depth first search: prioritizes children
    close_set = set_closed_set(frontier[0], close_set)
    if not children:
        frontier.pop(0)
        set_current_state(frontier, goal, close_set)
    else:
        for i in children:
            frontier.insert(0, i)
        set_current_state(frontier, goal, close_set)


def set_closed_set(state, close_set):
    if state not in close_set:
        close_set.append(state)
    if len(close_set) == math.factorial(9):
        print("Max possible combination")
    return close_set


# Finding children of current (2)
def find_children(frontier, current_state, goal, close_set):
    children = []

    # Calling neighbors function to locate the neighbors of null, thus locating the children
    neighbors = find_neighbors(current_state, close_set)

    for z in range(len(neighbors)):
        # Resetting child with current state information after each iteration.
        # This way, after finding each child we can reset the variable to look for the rest
        child = copy.deepcopy(current_state)
        # Searching for the null and neighbors to swap them
        for i in range(3):
            for j in range(3):
                if current_state[i][j] is None:
                    break
            else:
                continue
            break
        for x in range(3):
            for y in range(3):
                if current_state[x][y] == neighbors[z]:
                    child[x][y], child[i][j] = child[i][j], child[x][y]

                    break
            else:
                continue
            break
        children.append(child)

    set_frontier(frontier, children, goal, close_set)

# Finding neighbors of null cell (3)
def find_neighbors(current_state, close_set):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if current_state[i][j] is None:
                if j == 0:
                    if i == 0:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i][j + 1])
                    if i == 1:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j + 1])
                    if i == 2:
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j + 1])
                if j == 1:
                    if i == 0:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i][j + 1])
                        neighbors.append(current_state[i][j - 1])
                    if i == 1:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j + 1])
                        neighbors.append(current_state[i][j - 1])
                    if i == 2:
                        neighbors.append(current_state[i][j+1])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j - 1])
                if j == 2:
                    if i == 0:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i][j - 1])
                    if i == 1:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j - 1])
                    if i == 2:
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j - 1])
    return neighbors


# Creating initial state (1)
def creating_initial_state():
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8]         # Available numbers that can be used in puzzle
    init_state = [[0, 0, 0], [0, None, 0], [0, 0, 0]]   # Initializing the list

    for i in range(3):
        for j in range(3):
            if init_state[i][j] is not None:
                x = random.choice(possible_numbers)     # Choosing random number from possible numbers
                possible_numbers.remove(x)              # Removing the number that was chosen from possible numbers
                init_state[i][j] = x                    # Assigning number to puzzle's cell
    print_array(init_state)
    return init_state


def print_array(e):                              # Print list as array (N)
    for i in range(3):
        for j in range(3):
            if e[i][j] is None:
                print("X", end=' ')
            else:
                print(e[i][j], end=' ')
        print()
    print("\n")


if __name__ == "__main__":
    sys.setrecursionlimit(10**9)
    main()
