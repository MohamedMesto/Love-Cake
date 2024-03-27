import random

class Game_Board:
    '''
    Game Board initialization and other related Functions:
        - place_ship -->> Place a ship on the Game_Board
        - display  -->>   Display the Game_Board
        - 
    '''
    def __init__(self, game_size):
        # Initialize the Game_Board with a given game_size
        self.game_size = game_size

        # Create a 2D grid representing the Game_Board filled with 'O's
        self.grid = [['O' for _ in range(game_size)] for _ in range(game_size)]
        
        # List to store the ships' positions
        self.ships = []


    def place_ship(self, ship):
        x, y, game_size, orientation = ship
        if orientation == 'h':
            # If the orientation is horizontal, place the ship horizontally
            for i in range(game_size):
                self.grid[y][x + i] = 'X'
        else:
            # If the orientation is vertical, place the ship vertically
            for i in range(game_size):
                self.grid[y + i][x] = 'X'

        # Add the ship's position to the list of ships
        self.ships.append(ship)

    def display(self, hide_ships=False):
        print("  " + " ".join(str(i) for i in range(self.game_size)))
        for i in range(self.game_size):
            row = " ".join(self.grid[i][j] if not hide_ships or self.grid[i][j] == 'O' else 'O' for j in range(self.game_size))
            print(f"{i} {row}")
