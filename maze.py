import os
from random import randint
import readchar

""" Este programa es un juego de culebrita, muy simple, y requiere ser ejecutado en terminal para poder jugarse

    se maneja con las teclas W A S D, y se sale con T"""

class Maze:

    def __init__(self):
        self.ongame = True
        self.width = 15
        self.height = 15
        self.top_n_buttom = "+" + ("-" * 3 * self.width) + "+"
        self.snake = [[5, 5],[5, 4]]
        self.points = list(Maze.objects_gen())
        self.round_count = 1
        self.mov_vector = [0, 0]

# metodo que toma un caracter y lo transforma en un vector de movimiento, t o T para salir"
    def char_to_vector(self):
        direction = readchar.readchar()

        if direction == "w" or direction == "W":
            self.mov_vector = [-1, 0]
        elif direction == "a" or direction == "A":
            self.mov_vector = [0, -1]
        elif direction == "s" or direction == "S":
            self.mov_vector = [1, 0]
        elif direction == "d" or direction == "D":
            self.mov_vector = [0, 1]
        elif direction == direction == "t" or direction == "T":
            self.mov_vector = [0, 0]
            self.ongame = False

# Toma el valor de la cabeza, le reasigna uno nuevo sumandole el vector de movimiento, luego se inserta en la serpierte
# en la parte inicial y se borra el valor de la cola
    def movement(self):
        self.head = self.snake[0]
        self.new_head = []
        for i in range(len(self.head)):
           self.new_head.append(self.head[i] + self.mov_vector[i])
        self.snake.insert(0, self.new_head)
        self.snake.pop()
        return

# Metodo de crear puntos
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

                if [mark_pointy, mark_pointx] in self.snake:
                    print(" @ ", end="")

                    self.add_tail()

                elif [mark_pointy, mark_pointx] in self.points:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print("|")
        print(self.top_n_buttom)
        print(self.snake)

    def limit_interaction(self):
        if self.snake[0][0] > self.height - 1:
            self.snake[0][0] = 0
        if self.snake[0][0] < 0:
            self.snake[0][0] = self.height - 1
        if self.snake[0][1] > self.width - 1:
            self.snake[0][1] = 0
        if self.snake[0][1] < 0:
            self.snake[0][1] = self.width - 1

    def start_maze(self):
        while self.ongame:
            self.map_generator()
            self.char_to_vector()
            self.movement()
            self.limit_interaction()
            self.collision()
            os.system("cls")

    def add_tail(self):
        if self.snake[0] in self.points:
            self.snake.insert(0, self.snake[0])
            self.points.remove(self.snake[0])

    def collision(self):
        self.head = self.snake[0]
        if self.head in self.snake[1:]:
            self.ongame = False


def main():
    partida = Maze()
    partida.start_maze()


if __name__ == '__main__':
    main()
