import random
import copy
import sys


def main():
    # Setting initial state
    initial_state = creating_initial_state()
    # Debug code
    # initial_state = [[1, 2, 3], [4, 5, 6], [7, None, 8]]
    # Setting puzzle goal
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
    # Initializing frontier and setting initial state as frontier
    frontier = []
    frontier.insert(0, initial_state)
    # Initializing close set
    close_set = []
    # Starting solution
    solution(frontier, goal, close_set)


def solution(frontier, goal, close_set):
    # Setting current state as the initial state for first iteration
    current_state = set_current_state(frontier)
    while current_state != goal:
        # Popping first element of frontier (the one that is about to hbe examined)
        frontier.pop(0)
        # Debug code
        print("Frontier: ", len(frontier), " \t", "Close set: ", len(close_set))
        # If current state has not been examined yet,
        # find its children, put them in frontier and insert state in close set
        if current_state not in close_set:
            children = find_children(current_state)
            frontier = set_frontier(frontier, children)
            close_set = set_close_set(current_state, close_set)
        # If frontier is empty, a solution cannot be found
        if not frontier:
            print("Searching frontier is empty. \nCould not find solution. \nExiting program...")
            sys.exit()
        current_state = set_current_state(frontier)

    # This code will run only if the above while loop is escaped, meaning, a solution has been found
    print("Solution found! \nSteps: ")
    for i in close_set:
        print_array(i)
    print_array(goal)
    print("Solution found! See steps above.")
    print("Number of steps for solution: ")
    print(len(close_set))
    sys.exit()


# Setting new current state that is to be examined
def set_current_state(frontier):
    new_current_state = frontier[0]
    return new_current_state


# Finding children of current state
def find_children(current_state):
    children = []
    # Calling neighbors function to locate the neighbors of null, thus locating the children
    neighbors = find_neighbors(current_state)

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
    return children


# Finding neighbors of null cell of current state
def find_neighbors(current_state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if current_state[i][j] is None:
                if j == 0:
                    if i == 0:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i][j + 1])
                    elif i == 1:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j + 1])
                    else:
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j + 1])
                elif j == 1:
                    if i == 0:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i][j + 1])
                        neighbors.append(current_state[i][j - 1])
                    elif i == 1:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j + 1])
                        neighbors.append(current_state[i][j - 1])
                    else:
                        neighbors.append(current_state[i][j + 1])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j - 1])
                else:
                    if i == 0:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i][j - 1])
                    elif i == 1:
                        neighbors.append(current_state[i + 1][j])
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j - 1])
                    else:
                        neighbors.append(current_state[i - 1][j])
                        neighbors.append(current_state[i][j - 1])
    return neighbors


# Setting close set
def set_close_set(state, close_set):
    close_set.append(state)
    return close_set


# Setting frontier
def set_frontier(frontier, children):
    # Inserting children in frontier. Dfs algorithm prioritizes children, thus, children will be inserted first
    for i in children:
        frontier.insert(0, i)
    return frontier


# Creating initial state
def creating_initial_state():
    # Available numbers that can be used in puzzle
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    # Initializing the list
    init_state = [[0, 0, 0], [0, None, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            if init_state[i][j] is not None:
                # Choosing random number from possible numbers
                x = random.choice(possible_numbers)
                # Removing the number that was chosen from possible numbers
                possible_numbers.remove(x)
                # Assigning number to puzzle's cell
                init_state[i][j] = x
    print("Initial state: ")
    print_array(init_state)
    return init_state


# Print list as array
def print_array(e):
    for i in range(3):
        for j in range(3):
            if e[i][j] is None:
                print("X", end=' ')
            else:
                print(e[i][j], end=' ')
        print()
    print("\n")


if __name__ == "__main__":
    main()
