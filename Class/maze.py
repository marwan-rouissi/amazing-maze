from Class.cell import Cell
import random
from PIL import Image, ImageDraw

class Maze:
    
    def __init__(self, n:int) -> None:
        self.n = n
        # self.name = name
        self.entrance = (0, 0)
        self.exit = (n - 1, n - 1)
        self.board = [[Cell(i, j) for j in range(n)] for i in range(n)]
        self.neighbors = {"LEFT": None, "RIGHT": None, "UP": None, "DOWN": None}
        self.stack = []
        self.iteration = 0
        self.visited = set()

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
            return 
        
        """Check if the cell has any unvisited neighbours"""
        self.visited.add(cell.pos)

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
        """Replace ids list with a set -> faster (code optimization))"""
        # ids = []
        ids = set()

        iteration = 0
        """Assign an id to each cell"""
        for cell in self.board:
            for c in cell:
                c.id = iteration
                # ids.(c.id)
                ids.add(c.id)
                iteration += 1
        
        r = 0

        """While there are still ids in the list of ids"""
        # while len(ids) > 1:
        while r < (self.n*self.n)-1:
            # id = random.choice(ids)
            id = random.choice(tuple(ids))
            """Find the cell with the id"""
            for cell in self.board:
                for c in cell:
                    if c.id == id:
                        current_cell = c
        
            """Check the neighbours of the cell"""
            self.check_neighbours(current_cell.pos)
            directions = []
            for direction in self.neighbors:
                """Check if the neighbour exists"""
                if self.neighbors[direction] is not None:
                    """If the neighbour is unvisited, append the direction to the list of possible directions"""
                    if self.board[self.neighbors[direction][0]][self.neighbors[direction][1]].id != current_cell.id:
                        directions.append(direction)
            """If the cell has unvisited neighbours, choose a random direction and break the wall between the cell and the next cell"""
            if len(directions) > 0:
                direction = random.choice(directions)
                next_cell = self.board[self.neighbors[direction][0]][self.neighbors[direction][1]]

                """Break the wall between the cell and the next cell"""
                if current_cell.id != next_cell.id:
                    current_cell.break_wall(direction, next_cell)
                    r += 1
                    """Change the id of the next cell to the id of the cell"""
                    if current_cell.id > next_cell.id:
                        id_to_remove = current_cell.id
                        """Remove the id of the cell from the list of ids"""
                        if current_cell.id in ids:
                            # ids.remove(current_cell.id)
                            ids.discard(current_cell.id)
                        """Change the id of all the cells with the id of the next cell"""
                        for cell in self.board:
                            for c in cell:
                                if c.id == id_to_remove:
                                    c.id = next_cell.id
                        """Change the id of the cell to the id of the next cell"""
                    elif current_cell.id < next_cell.id:
                        id_to_remove = next_cell.id
                        """Remove the id of the next cell from the list of ids"""
                        if next_cell.id in ids:
                            # ids.remove(next_cell.id)
                            ids.discard(next_cell.id)
                        """Change the id of all the cells with the id of the cell"""
                        for cell in self.board:
                            for c in cell:
                                if c.id == id_to_remove:
                                    c.id = current_cell.id

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
                print(cell, end=" ")
            print("")
        print()
    
    """Save the maze as a file.txt"""
    def save_maze(self, name:str):
        maze = self.convert_to_maze()
        with open(f"mazes/{name}.txt", "w") as f:
            for lane in maze:
                for cell in lane:
                    f.write(cell)
                f.write("\n")

    """Print the maze in the console"""
    def print_maze(self):
        self.board[0][0].walls["LEFT"] = False
        self.board[self.n - 1][self.n - 1].walls["RIGHT"] = False

        for i in range(self.n):
            print(" _", end="")
        print("")
        for lane in self.board:
            if lane[0].walls["LEFT"] == True:
                print("|", end="")
            else:
                print(" ", end="")
            for cell in lane:
                if cell.walls["DOWN"] == True:
                    print("_", end="")
                else:
                    print(" ", end="")
                if cell.walls["RIGHT"] == True:
                    print("|", end="")
                else:
                    print(" ", end="")
            print("")
    
        """Ascii to JPG"""
    def ascii_to_jpg(self, name:str):
        maze = self.convert_to_maze()
        img = Image.new("RGB", (len(maze) * 10, len(maze) * 10), color="white")
        draw = ImageDraw.Draw(img)
        for i in range(len(maze)):
            for j in range(len(maze)):
                if maze[i][j] == "#":
                    draw.rectangle(((j * 10, i * 10), (j * 10 + 10, i * 10 + 10)), fill="black")
                elif maze[i][j] == ".":
                    draw.rectangle(((j * 10, i * 10), (j * 10 + 10, i * 10 + 10)), fill="white")
                elif maze[i][j] == "o":
                    draw.rectangle(((j * 10, i * 10), (j * 10 + 10, i * 10 + 10)), fill="red")
                elif maze[i][j] == "*":
                    draw.rectangle(((j * 10, i * 10), (j * 10 + 10, i * 10 + 10)), fill="purple")
                elif maze[i][j] == "S":
                    draw.rectangle(((j * 10, i * 10), (j * 10 + 10, i * 10 + 10)), fill="green")
                elif maze[i][j] == "E":
                    draw.rectangle(((j * 10, i * 10), (j * 10 + 10, i * 10 + 10)), fill="blue")
        img.save(f"mazes/{name}.jpg")