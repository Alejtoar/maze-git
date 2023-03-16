import os
from random import randint
import readchar


class Maze:

    def __init__(self):
        self.ongame = True
        self.width = 15
        self.height = 15
        self.top_n_buttom = "+" + ("-" * 3 * self.width) + "+"
        self.actual_pos = [5, 5]
        self.points = list(Maze.objects_gen())
        self.round_count = 1
        self.mov_vector = [0, 0]

    def char_to_vector(self):
        direction = readchar.readchar()

        if direction == "w" or direction == "W":
            self.mov_vector = [-1, 0]
        elif direction == "a" or direction ==  "A":
            self.mov_vector = [0, -1]
        elif direction == "s" or direction ==  "S":
            self.mov_vector = [1, 0]
        elif direction == "d" or direction ==  "D":
            self.mov_vector = [0, 1]
        elif direction == direction == "t" or direction ==  "T":
            self.mov_vector = [0, 0]
            self.ongame = False

    def sum_of_mov_vector(self):
        for i in range(len(self.actual_pos)):
            self.actual_pos[i] = self.actual_pos[i] + self.mov_vector[i]
        return

    @staticmethod
    def objects_gen():
        objects = []
        while len(objects) != 3:
            objeto = [randint(0, 14), randint(0, 14)]
            if objeto not in objects:
                objects.append(objeto)
        return objects

    def map_generator(self):
        if self.round_count % 9 == 0:
            self.points = list(Maze.objects_gen())
        self.round_count += 1
        print(self.top_n_buttom)

        for i in range(self.height):
            mark_pointy = i
            print("|", end="")
            for j in range(self.width):
                mark_pointx = j
                if mark_pointy == self.actual_pos[0] and mark_pointx == self.actual_pos[1]:
                    print(" @ ", end="")
                    if self.actual_pos in self.points:
                        self.points.remove(self.actual_pos)
                elif [mark_pointy, mark_pointx] in self.points:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print("|")
        print(self.top_n_buttom)

    def movement(self):
        if self.actual_pos[0] > self.height - 1:
            self.actual_pos[0] = 0
        if self.actual_pos[0] < 0:
            self.actual_pos[0] = self.height - 1
        if self.actual_pos[1] > self.width - 1:
            self.actual_pos[1] = 0
        if self.actual_pos[1] < 0:
            self.actual_pos[1] = self.width - 1


    def start_maze(self):
        while self.ongame:
            self.map_generator()
            self.char_to_vector()
            self.sum_of_mov_vector()
            self.movement()
            os.system("cls")

def main():
    partida = Maze()
    partida.start_maze()

if __name__ == '__main__':
    main()
