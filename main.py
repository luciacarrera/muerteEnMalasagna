import random
import math

NUMBER_OF_GROUPS = 4
MIN_ALIVE_PEOPLE = 3


def read_names(file_path):
    try:
        with open(file_path, "r") as file:
            names = file.readlines()
            names = [name.strip() for name in names]
        return names
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []


def get_alive_and_dead(names):
    alive = []
    dead = []
    for name in names:
        if name[0].lower() == "x":
            dead.append(name)
        else:
            alive.append(name)
    return alive, dead


def main():
    # get participants
    file_path = "nombres.txt"
    people = read_names(file_path)

    # separate alive and dead
    alive, dead = get_alive_and_dead(people)

    # get amount of people in each group
    group_size = math.ceil(len(people) / NUMBER_OF_GROUPS)

    # create an array with Number of groups subarrays
    groups = [[] for _ in range(NUMBER_OF_GROUPS)]

    # assign minimum alive people to each group only if there are enough alive people
    for i in range(NUMBER_OF_GROUPS):
        if len(alive) > MIN_ALIVE_PEOPLE:
            for j in range(MIN_ALIVE_PEOPLE):
                person = alive.pop(random.randint(0, len(alive) - 1))
                groups[i].append(person)

    # assign the rest of the alive people to the groups with alive people
    for i in range(NUMBER_OF_GROUPS):
        if len(alive) > 0 and len(groups[i]) > 0 and len(groups[i]) < group_size:
            person = alive.pop(random.randint(0, len(alive) - 1))
            groups[i].append(person)

    # assign dead people to the groups
    for i in range(NUMBER_OF_GROUPS):
        if len(dead) > 0 and len(groups[i]) < group_size:
            person = dead.pop(random.randint(0, len(dead) - 1))
            groups[i].append(person)

    # print the groups
    for i, group in enumerate(groups):
        print(f"Grupo {i + 1}:")
        for person in group:
            print(f"  - {person}")
        print()


if __name__ == "__main__":
    main()
