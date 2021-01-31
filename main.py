"""
    Main module
"""
from controller.board_service import BoardService
from model.board import Board
from ui.ui import Console

if __name__ == "__main__":
    board = Board()
    board_service = BoardService(board)
    console = Console(board_service)

    console.run_console()
