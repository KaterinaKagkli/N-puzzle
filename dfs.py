import random
import copy


def main():
    initial_state = creating_initial_state()
    goal = [[1, 4, 7], [2, 5, 8], [3, 6, None]]         # Setting puzzle goal
    frontier = []
    close_set = []

    # Starting solution with the initial state as first iteration
    begin_solution(initial_state)


def begin_solution(initial_state):
    find_children(initial_state)  # Used to find neighbors the first time


def set_current_state(frontier):
    new_current_state = frontier[0]
    find_children(new_current_state)


def set_frontier(children):
    #Todo: append or insert children list (individualy)
    pass


# Finding children of current (2)
def find_children(current_state):
    # Calling neighbors function to locate the neighbors of null, thus locating the children
    neighbors = find_neighbors(current_state)

    children = []
    for z in range(len(neighbors)):
        # Resetting child with current state information after each iteration.
        # This way, after finding each child we can reset the variable to look for the rest
        child = current_state
        # Searching for the null and neighbors to swap them
        for i in range(3):
            for j in range(3):
                if current_state[i][j] is None:
                    for x in range(3):
                        for y in range(3):
                            if current_state[x][y] == neighbors[z]:
                                child[i][j], child[x][y] = current_state[x][y], current_state[i][j]
                                children.append(child)
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
            else:
                continue
            break

    #Todo: Set frontier(children)


# Finding neighbors of null cell (3)
def find_neighbors(current_state):
    # Todo: if current_state in close_set:                # If current state exists in closed set skip this iteration
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
