import random
import copy


def main():
    initial_state = creating_initial_state()
    goal = [[1, 4, 7], [2, 5, 8], [3, 6, None]]         # Setting puzzle goal
    frontier = []
    close_set = []

    # Setting initial state as current state for the first iteration
    current_state = initial_state
    children = []
    children.append(find_children(current_state)) # Used to find neighbors the first time


def set_current_state(frontier):
    new_current_state = frontier[0]
    find_children(new_current_state)


def set_frontier(children):
    #Todo: append or insert children list (individualy)
    pass


def find_children(current_state):                                    # Finding children(3)
    neighbors = find_neighbors(current_state)
    #Todo: swap null with neighbors
    #Todo: Set frontier(children)


def find_neighbors(current_state):                # Finding neighbors of null cell (2)
    # Todo: if current_state in close_set:                         # If current state exists in closed set skip this iteration
    #     return
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
                        neighbors.append(current_state[i + 1][j])
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


def print_array(e):                                     # Print list as array (N)
    for i in range(3):
        for j in range(3):
            if e[i][j] is None:
                print("X", end=' ')
            else:
                print(e[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
