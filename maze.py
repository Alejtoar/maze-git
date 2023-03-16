import os
from random import randint

import readchar


def char_to_vector():
    direction = readchar.readchar()
    if direction == "w":
        return -1, 0
    elif direction == "a":
        return 0, -1
    elif direction == "s":
        return 1, 0
    elif direction == "d":
        return 0, 1

def sum_of_arrays(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])
    return new_list

def objects_gen():
    objects = []
    while len(objects) != 3:
        objeto = [randint(0, 14), randint(0, 14)]
        if objeto not in objects:
            objects.append(objeto)
    return objects

def map_generator():
    pass
def movement():
    pass


def main():
    ongame = True
    width = 15
    height = 15
    top_n_buttom = "+" + ("-" * 3 * width ) + "+"
    actual_pos = [5, 5]
    points = list(objects_gen())
    round_count = 1
    while ongame:
        if round_count % 9 == 0:
            points = list(objects_gen())
        round_count += 1
        print(top_n_buttom)
        for i in range(height):
            mark_pointy = i
            print("|", end = "")
            for j in range(width):
                mark_pointx = j
                if mark_pointy == actual_pos[0] and mark_pointx == actual_pos[1]:
                    print(" @ ", end = "")
                    if actual_pos in points:
                        points.remove(actual_pos)
                elif [mark_pointy,mark_pointx] in points:
                    print(" * ", end = "")
                else:
                    print("   ", end = "")
            print("|")
        print(top_n_buttom)
        new_pos = list(sum_of_arrays(actual_pos, char_to_vector()))
        if new_pos[0] > height - 1:
            new_pos[0] = 0
        if new_pos[0] < 0:
            new_pos[0] = height - 1
        if new_pos[1] > width - 1:
            new_pos[1] = 0
        if new_pos[1] < 0:
            new_pos[1] = width - 1

        actual_pos = new_pos
        os.system("cls")

if __name__ == '__main__':
    main()
