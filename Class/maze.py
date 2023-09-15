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
            print("visited all cells")
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
            next_cell = self.board[self.stack[-1][0]][self.stack[-1][1]]
        
            """If the cell has unvisited neighbours, choose a random direction and break the wall between the cell and the next cell"""
        else:
            self.stack.append(cell.pos)  
            direction = random.choice(directions)
            next_cell = self.board[self.neighbors[direction][0]][self.neighbors[direction][1]]
            cell.break_wall(direction, next_cell)
        self.recursive(next_cell.pos)
    
    """Kruskal's algorithm"""
    def kruskal(self):
        ids = []
        iteration = 0
        for cell in self.board:
            for c in cell:
                c.id = iteration
                ids.append(c.id)
                iteration += 1
        
        current_cell = self.board[0][0]
        ids.remove(current_cell.id)

        while len(ids) > 0:

            self.check_neighbours(current_cell.pos)
            directions = []
            """Check the neighbours of the cell"""
            for direction in self.neighbors:
                """Check if the neighbour exists"""
                if self.neighbors[direction] is not None:
                    """If the neighbour is unvisited, append the direction to the list of possible directions"""
                    if self.board[self.neighbors[direction][0]][self.neighbors[direction][1]].id != current_cell.id:
                        directions.append(direction)
            
            if len(directions) > 0:
                direction = random.choice(directions)
                next_cell = self.board[self.neighbors[direction][0]][self.neighbors[direction][1]]

                """Break the wall between the cell and the next cell"""
                if current_cell.id != next_cell.id:
                    current_cell.break_wall(direction, next_cell)
                    """Change the id of the next cell to the id of the cell"""
                    if current_cell.id > next_cell.id:
                        if current_cell.id in ids:
                            ids.remove(current_cell.id)
                        current_cell.id = next_cell.id

                    elif current_cell.id < next_cell.id:
                        if next_cell.id in ids:
                            ids.remove(next_cell.id)

                        next_cell.id = current_cell.id

                current_cell = next_cell
            else:
                id = random.choice(ids)
                # print(f"random id: {id}")
                for cell in self.board:
                    for c in cell:
                        if c.id == id:
                            current_cell = c

    """Convert the board to a list of lists with the correct format for the maze (labyrinth: cells with walls and paths)"""
    def convert_to_maze(self):
        labyrinth = []
        wall = ["#"]
        pathSide = []
        pathInter = ["#"]
        for i in range(self.n):
            for j in range(self.n):          
                if i == 0 and j == 0:
                    pathSide.append(".")
                if i == 0:
                    wall.append("#")
                    wall.append("#")
                if self.board[i][j].walls["RIGHT"] == False:
                    pathSide.append(".")
                    pathSide.append(".")
                elif self.board[i][j].walls["RIGHT"] == True:
                    pathSide.append(".")
                    pathSide.append("#")
                if self.board[i][j].walls["DOWN"] == False:
                    pathInter.append(".")
                    pathInter.append("#")
                elif self.board[i][j].walls["DOWN"] == True:
                    pathInter.append("#")
                    pathInter.append("#")
                if i == self.n - 1 and j == self.n - 1:
                    pathSide.pop()
                    pathSide.append(".")
            if i == 0:
                labyrinth.append(wall)
            labyrinth.append(pathSide)
            pathSide = ["#"]
            labyrinth.append(pathInter)
            pathInter = ["#"]
        return labyrinth

    """Draw the maze"""
    def draw_maze(self):
        maze = self.convert_to_maze()
        print()
        for lane in maze:
            for cell in lane:
                print(cell, end="")
            print("")
        print()
        return maze
    
    """Save the maze as a file.txt"""
    def save_maze(self):
        with open(f"{self.name}.txt", "w") as f:
            for lane in self.draw_maze():
                for cell in lane:
                    f.write(cell)
                f.write("\n")
        print(f"File {self.name}.txt saved")
        return f"{self.name}.txt"