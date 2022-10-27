board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def main():
    init_board()
    display_board()


def init_board() -> None:
    """Fills up the board with blanks"""
    for row in range(3):
        for col in range(3):
            board[row][col] = " "


def display_board() -> None:
    print("  0  {}|{}|{}".format(board[0][0], board[0][1], board[0][2]))
    print("    --+-+--")
    print("  1  {}|{}|{}".format(board[1][0], board[1][1], board[1][2]))
    print("    --+-+--")
    print("  2  {}|{}|{}".format(board[2][0], board[2][1], board[2][2]))
    print("     0 1 2 ")



def display_board2() -> None:
    for row in range(3):
        print(f"\t{row} ", end="")
        for col in range(3):
            print(f"{board[row][col]} ", end="")
        print()
    print("\t  0 1 2 ")




if __name__ == "__main__":
    main()