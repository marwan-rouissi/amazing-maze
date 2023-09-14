from Class.cell import Cell
import random

class Maze:
    
    def __init__(self, n:int, name:str="Maze") -> None:
        self.n = n
        self.name = name
        self.entrance = (0, 0)
        self.exit = (n - 1, n - 1)
        self.board = [[Cell(i, j) for j in range(n)] for i in range(n)]
        self.neighbors = {"LEFT": None, "RIGHT": None, "UP": None, "DOWN": None}
        self.stack = []
        self.iteration = 0
        self.visited = []

    """Check the neighbours of the cell"""
    def check_neighbours(self, cell:tuple) -> None:
        x = cell[0]
        y = cell[1]
        if x > 0:
            self.neighbors["UP"] = (x - 1, y)
        else:
            self.neighbors["UP"] = None

        if y > 0:
            self.neighbors["LEFT"] = (x, y - 1)
        else:
            self.neighbors["LEFT"] = None

        if x < self.n - 1:
            self.neighbors["DOWN"] = (x + 1, y)
        else:
            self.neighbors["DOWN"] = None

        if y < self.n - 1:
            self.neighbors["RIGHT"] = (x, y + 1)
        else:
            self.neighbors["RIGHT"] = None
       
    """Recursive backtracking algorithm"""
    def recursive(self, pos) -> None:
        cell = self.board[pos[0]][pos[1]]
        self.check_neighbours(cell.pos)
        cell.isvisited = True
        directions = []
        """Check if all cells are visited"""
        if len(self.visited) == self.n*self.n:
            print(len(self.visited))
            print(self.n*self.n)
            print("visited all cells")
            print(f"stack: {self.stack}")
            print(f"visited: {self.visited}")
            return 
        
        """Check if the cell has any unvisited neighbours"""
        if cell.pos not in self.visited:
            self.visited.append(cell.pos)

        """Check the neighbours of the cell"""
        for direction in self.neighbors:
            """Check if the neighbour exists"""
            if self.neighbors[direction] is not None:
                """If the neighbour is unvisited, append the direction to the list of possible directions"""
                if self.board[self.neighbors[direction][0]][self.neighbors[direction][1]].isvisited == False:
                    directions.append(direction)

        """If the cell has no unvisited neighbours, pop the stack and call the function again"""
        if directions == []:
            self.stack.pop()
            print(f"stack before recursion: {self.stack}")
            print(f"visited: {self.visited}")
            next_cell = self.board[self.stack[-1][0]][self.stack[-1][1]]
        
            """If the cell has unvisited neighbours, choose a random direction and break the wall between the cell and the next cell"""
        else:
            self.stack.append(cell.pos)  
            print(f"cell pos: {cell.pos}")
            print(f"neighbours: {self.neighbors}")
            print(f"directions: {directions}")
            direction = random.choice(directions)
            print(f"possible directions: {directions}")
            print(f"direction: {direction}")
            next_cell = self.board[self.neighbors[direction][0]][self.neighbors[direction][1]]

            print(f"stack: {self.stack}")
            print(f"next cell pos: {next_cell.pos}")
            cell.break_wall(direction, next_cell)

        self.recursive(next_cell.pos)
    
# maze = Maze(3)
# maze.recursive(maze.entrance)