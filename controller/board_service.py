"""
    Board service module
"""
from prettytable import PrettyTable
import random
import copy


class StoreException(Exception):
    pass


class GameOverException(StoreException):
    pass


class Snake:
    def __init__(self):
        self.__dimension = 3
        self.__direction = "up"
        self.__coordinates = None

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    def get_head_coordinates(self):
        return self.__coordinates[0]

    def get_tail_coordinates(self):
        return self.__coordinates[-1]


class BoardService:
    def __init__(self, board):
        self.__board = board
        self.__snake = Snake()

    def create_pretty_table(self):
        table = PrettyTable()
        board_info = self.__board.get_board()
        table.add_rows(board_info)
        return table

    def get_center_snake_coordinates(self):
        """
        Computes the coordinates that need to be set for the snake to be at
        the center of the board.
        :return:
        """
        board_dim = self.__board.dimension

        coordinates = [[board_dim // 2 - 1, board_dim // 2], [board_dim // 2, board_dim // 2],
                       [board_dim // 2 + 1, board_dim // 2]]

        return coordinates

    def set_snake_coordinates(self):
        """
        Sets the snake coordinates so that the snake is in the center of the board
        :return:
        """
        self.__snake.coordinates = self.get_center_snake_coordinates()

    def place_snake(self):
        """
        Places the snake on the board
        :return:
        """
        self.set_snake_coordinates()
        self.__board.mark_snake(self.__snake.coordinates)

    def place_random_apples(self):
        """
        Places the amount of apples necessary randomly on the board.
        :return:
        """
        while self.__board.current_apples < self.__board.apples:
            random_x = random.randint(0, self.__board.dimension - 1)
            random_y = random.randint(0, self.__board.dimension - 1)

            if not self.__board.board_is_marked(random_x, random_y) and self.__board.position_free(random_x, random_y):
                self.__board.place_apple(random_x, random_y)
                self.__board.current_apples = self.__board.current_apples + 1

    def bend_snake_right(self, nr_steps=1):
        """
        Moves the snake to the right one step if it is not already facing rightward.
        :return:
        """

        if self.__snake.direction == "left":
            print("You cannot do a 180!")
            return

        for x in range(nr_steps):
            head_x, head_y = self.__snake.get_head_coordinates()

            # Checking if game over
            if head_x + 1 >= self.__board.dimension or head_y + 1 >= self.__board.dimension\
                    or self.__board.marked_by_snake(head_x + 1, head_y + 1):
                raise GameOverException("Game over!")

            # Unmark snake
            self.__board.unmark_snake(self.__snake.coordinates)

            # Moving snake

            coordinates = self.__snake.coordinates
            print(coordinates)
            # For each coordinate except the head, take the value of the coordinate after it = "slither"
            for x in range(len(coordinates) - 1, 0, -1):
                coordinates[x] = copy.deepcopy(coordinates[x - 1])

            # Moving head rightward
            # coordinates[0][0] = coordinates[0][0] + 1
            coordinates[0][1] = coordinates[0][1] + 1

            # Updating snake coordinates and writing snake
            self.__snake.coordinates = coordinates
            print(coordinates)
            nr_apples = self.__board.mark_snake(self.__snake.coordinates)
            # If the snake eats an apple, add a point
            if nr_apples == 1:
                self.__snake.coordinates.append([0, 0])
            self.__snake.direction = "right"

    def bend_snake_up(self, nr_steps=1):
        """
        Moves the snake to the right one step if it is not already facing rightward.
        :return:
        """

        if self.__snake.direction == "down":
            print("You cannot do a 180!")
            return

        for x in range(nr_steps):
            head_x, head_y = self.__snake.get_head_coordinates()

            # Checking if game over
            if head_x - 1 < 0 or head_y - 1 < 0\
                    or self.__board.marked_by_snake(head_x - 1, head_y - 1):
                raise GameOverException("Game over!")

            # Unmark snake
            self.__board.unmark_snake(self.__snake.coordinates)

            # Moving snake

            coordinates = self.__snake.coordinates
            print(coordinates)
            # For each coordinate except the head, take the value of the coordinate after it = "slither"
            for x in range(len(coordinates) - 1, 0, -1):
                coordinates[x] = copy.deepcopy(coordinates[x - 1])

            # Moving head rightward
            coordinates[0][0] = coordinates[0][0] - 1

            # Updating snake coordinates and writing snake
            self.__snake.coordinates = coordinates
            print(coordinates)
            nr_apples = self.__board.mark_snake(self.__snake.coordinates)
            # If the snake eats an apple, add a point
            if nr_apples == 1:
                self.__snake.coordinates.append([0, 0])
            self.__snake.direction = "up"

    def bend_snake_left(self, nr_steps=1):
        """
        Moves the snake to the right one step if it is not already facing rightward.
        :return:
        """

        if self.__snake.direction == "right":
            print("You cannot do a 180!")
            return

        for x in range(nr_steps):
            head_x, head_y = self.__snake.get_head_coordinates()

            # Checking if game over
            if head_x + 1 >= self.__board.dimension or head_y - 1 < 0\
                    or self.__board.marked_by_snake(head_x + 1, head_y - 1):
                raise GameOverException("Game over!")

            # Unmark snake
            self.__board.unmark_snake(self.__snake.coordinates)

            # Moving snake

            coordinates = self.__snake.coordinates
            print(coordinates)
            # For each coordinate except the head, take the value of the coordinate after it = "slither"
            for x in range(len(coordinates) - 1, 0, -1):
                coordinates[x] = copy.deepcopy(coordinates[x - 1])

            # Moving head rightward
            # coordinates[0][0] = coordinates[0][0] + 1
            coordinates[0][1] = coordinates[0][1] - 1

            # Updating snake coordinates and writing snake
            self.__snake.coordinates = coordinates
            print(coordinates)
            nr_apples = self.__board.mark_snake(self.__snake.coordinates)
            # If the snake eats an apple, add a point
            if nr_apples == 1:
                self.__snake.coordinates.append([0, 0])

            self.__snake.direction = "left"

    def bend_snake_down(self, nr_steps=1):
        """
        Moves the snake to the right one step if it is not already facing rightward.
        :return:
        """

        if self.__snake.direction == "up":
            print("You cannot do a 180!")
            return

        for x in range(nr_steps):
            head_x, head_y = self.__snake.get_head_coordinates()

            # Checking if game over
            if head_x + 1 >= self.__board.dimension or head_y - 1 < 0\
                    or self.__board.marked_by_snake(head_x + 1, head_y):
                raise GameOverException("Game over!")

            # Unmark snake
            self.__board.unmark_snake(self.__snake.coordinates)

            # Moving snake

            coordinates = self.__snake.coordinates
            print(coordinates)
            # For each coordinate except the head, take the value of the coordinate after it = "slither"
            for x in range(len(coordinates) - 1, 0, -1):
                coordinates[x] = copy.deepcopy(coordinates[x - 1])

            # Moving head downward
            coordinates[0][0] = coordinates[0][0] + 1
            # coordinates[0][1] = coordinates[0][1] - 1

            # Updating snake coordinates and writing snake
            self.__snake.coordinates = coordinates
            print(coordinates)
            nr_apples = self.__board.mark_snake(self.__snake.coordinates)

            # If the snake eats an apple, add a point
            if nr_apples == 1:
                self.__snake.coordinates.append([0, 0])
            self.__snake.direction = "down"

    def get_snake_orientation(self):
        return self.__snake.direction
