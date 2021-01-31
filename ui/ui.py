"""
    Ui module
"""


class Console:
    def __init__(self, board_service):
        self.__board_service = board_service

    def run_console(self):
        self.__board_service.place_snake()
        self.__board_service.place_random_apples()

        while True:
            self.print_board()

            cmd = input("Command: ")
            li_words = cmd.split()

            # If command is move
            if li_words[0] == "move":
                orientation = self.__board_service.get_snake_orientation()
                if len(li_words) == 1:
                    if orientation == "up":
                        self.__board_service.bend_snake_up()
                    if orientation == "down":
                        self.__board_service.bend_snake_down()
                    if orientation == "left":
                        self.__board_service.bend_snake_left()
                    if orientation == "right":
                        self.__board_service.bend_snake_right()
                else:
                    if orientation == "up":
                        self.__board_service.bend_snake_up(int(li_words[1]))
                    if orientation == "down":
                        self.__board_service.bend_snake_down(int(li_words[1]))
                    if orientation == "left":
                        self.__board_service.bend_snake_left(int(li_words[1]))
                    if orientation == "right":
                        self.__board_service.bend_snake_right(int(li_words[1]))
            if li_words[0] == "right":
                self.__board_service.bend_snake_right()
            if li_words[0] == "up":
                self.__board_service.bend_snake_up()
            if li_words[0] == "left":
                self.__board_service.bend_snake_left()
            if li_words[0] == "down":
                self.__board_service.bend_snake_down()

    def print_board(self):
        print(self.__board_service.create_pretty_table())
