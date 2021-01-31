"""
    Board module
"""


class Board:
    def __init__(self):
        """
        Board initialization.
        Board is represented as a matrix
        """
        self.__dim, self.__apple_count = self.read_dims_and_apple_count()
        self.__board = [[' '] * self.__dim for x in range(self.__dim)]
        self.__current_apples = 0

    @property
    def dimension(self):
        return self.__dim

    @property
    def apples(self):
        return self.__apple_count

    @property
    def current_apples(self):
        return self.__current_apples

    @current_apples.setter
    def current_apples(self, current_apples):
        self.__current_apples = current_apples

    @staticmethod
    def read_dims_and_apple_count():
        """
        Reads the dimension of the board and the number of apples from the settings.properties file.
        In the file, they are formatted like this: *dimension*;*apple_count*
        :return:
        """
        dim = 0
        apple_count = 0

        try:
            file = open("settings.properties", "r")
            line = file.readline().strip()

            line = line.split(';')
            dim = int(line[0])
            apple_count = int(line[1])

            file.close()

        except Exception as ex:
            print(ex)  # log the error
            raise ex

        return dim, apple_count

    def get_board(self):
        return self.__board

    def mark_snake(self, coordinates):
        """
        Marks the board, placing the snake
        :param coordinates:
        :return: 1 if the snake's head meets an apple, 0 otherwies
        """

        nr_apples = 0

        if self.__board[coordinates[0][0]][coordinates[0][1]] == '.':
            nr_apples = 1

        # The first coordinate is that of the head
        self.__board[coordinates[0][0]][coordinates[0][1]] = '*'

        for x in range(1, len(coordinates)):
            self.__board[coordinates[x][0]][coordinates[x][1]] = '+'

        return nr_apples

    def unmark_snake(self, coordinates):
        """
        Unmarks the board, deleting the snake
        :param coordinates:
        :return:
        """
        # The first coordinate is that of the head
        self.__board[coordinates[0][0]][coordinates[0][1]] = ' '

        for x in range(1, len(coordinates)):
            self.__board[coordinates[x][0]][coordinates[x][1]] = ' '

    def board_is_marked(self, x, y):
        """
        Returns true if a certain position of the board is marked, false otherwise
        :return:
        """
        if self.__board[x][y] != ' ':
            return True
        return False

    def position_free(self, x, y):
        """
        Returns true if an apple can be placed at position [x][y].
        i.e. there are no apples adjacent to that position
        :param x:
        :param y:
        :return:
        """

        # Checking above
        if x - 1 >= 0:
            if y - 1 >= 0:
                if self.__board[x - 1][y - 1] == '.':
                    return False

            if self.__board[x - 1][y] == '.':
                return False

            if y + 1 < self.__dim:
                if self.__board[x - 1][y + 1] == '.':
                    return False

        # Checking to the left
        if y - 1 >= 0:
            if self.__board[x][y - 1] == '.':
                return False

            if x + 1 < self.__dim:
                if self.__board[x + 1][y - 1] == '.':
                    return False

        # Checking below
        if x + 1 < self.__dim:
            if self.__board[x + 1][y] == '.':
                return False

            if y + 1 < self.__dim:
                if self.__board[x + 1][y + 1] == '.':
                    return False

        # Checking to the right
        if y + 1 < self.__dim:
            if self.__board[x][y + 1] == '.':
                return False

        return True

    def place_apple(self, x, y):
        """
        Places an apple at board[x][y].
        :param x:
        :param y:
        :return:
        """
        self.__board[x][y] = '.'

    def marked_by_snake(self, x, y):
        """
        Returns true if a certain position is marked by the snake
        :param x:
        :param y:
        :return:
        """
        if self.__board[x][y] == '+':
            return True
        return False
