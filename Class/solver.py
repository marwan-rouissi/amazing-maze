import random
from PIL import Image, ImageDraw

class Solver:

    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.entrance = (1, 1)
        self.opening = (1, 0)
        self.exit = (self.n - 2, self.n - 2)
        self.path = []
        self.visited = []
        self.visited.append((1, 0))
        self.neighbors = {"LEFT": None, "RIGHT": None, "UP": None, "DOWN": None}

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
    def backtrack(self, pos) -> None:
        cell = pos
        self.check_neighbours(cell)
        directions = []

        """Check if the cell is the exit"""
        if cell == self.exit:
            print('')
            print("found exit")
            if self.opening in self.visited:
                self.visited.remove(self.opening)
            for cell in self.path:
                for visited in self.visited:
                    if visited not in self.path:
                        self.board[visited[0]][visited[1]] = "*"
                self.board[cell[0]][cell[1]] = "o"
            return self.board
        """Check if the cell has been visited otherwise add it to the visited lists"""
        if cell not in self.visited:
            self.visited.append(cell)
            self.path.append(cell)
        """Check the neighbours of the cell"""
        for direction in self.neighbors:
            """If the neighbour is unvisited, append the direction to the list of possible directions"""
            if self.board[self.neighbors[direction][0]][self.neighbors[direction][1]] != "#":
                if self.neighbors[direction] not in self.visited:
                    directions.append(direction)
        """Check if there are any valid moves"""
        if len(directions) > 0:
            """Choose a random direction"""
            direction = random.choice(directions)
            """Move to the next cell"""
            cell = self.neighbors[direction]
            """Check if the cell has been visited otherwise add it to the visited lists"""
            if cell not in self.visited:
                self.visited.append(cell)
                self.path.append(cell)
        else:
            """Pop the cell from the stack"""
            self.path.pop()
            """Move to the previous cell"""
            cell = self.path[-1]
        self.backtrack(cell)

    """Heuristic function"""
    def heuristic(self, cell:tuple, end:tuple) -> int:
        """Calculate the heuristic value"""
        h = abs(cell[0] - end[0]) + abs(cell[1] - end[1])
        return h    
    
    """reconstruct the path"""
    def reconstruct_path(self, parent:dict, current_cell:tuple) -> list:
        """Create a list of the path"""

        """Optimize the code
        using extend instead of append and reverse the list at the end"""
        # path = []
        # while current_cell in parent:
        #     path.append(current_cell)
        #     # path.extend(current_cell)
        #     current_cell = parent[current_cell]
        # return path[::-1]
    
        path = [self.exit]
        while current_cell in parent:
            path.extend([current_cell])
            current_cell = parent[current_cell]
        self.path = path[::-1]
        return 

    """A* algorithm"""
    def AStar(self) -> None:
        start = self.entrance
        end = self.exit
        open_list = []
        # open_list = set()
        closed_list = []
        # closed_list = set()
        h = self.heuristic(start, end)
        g = {start: 0}
        f = {start: h+g[start]}
        parent = {start: None}
        current_cell = start

        """Add the start cell to the open list"""
        open_list.append(start)
        # open_list.add(start)

        """While the open list is not empty"""
        while len(open_list) > 0:
            """sort the open list by f value"""
            open_list.sort(key=lambda x: f[x])
            # open_list = sorted(open_list, key=lambda x: f[x])
            # print(open_list)
            # open_list = sorted(open_list, key=lambda x: f[x])
            # print(open_list)
            """Remove the current node from the open list"""
            current_cell = open_list.pop(0)

            """if the current cell is the exit, stop the loop"""
            if current_cell == end:
                print("found exit")
                """Reconstruct the path and mark it with o, mark the explored cells with * """
                path = self.reconstruct_path(parent, current_cell)
                # self.reconstruct_path(parent, current_cell)
                for cell in self.path:
                    for visited in closed_list:
                        if visited not in self.path:
                            self.board[visited[0]][visited[1]] = "*"
                    self.board[cell[0]][cell[1]] = "o"
                return
            else:
                closed_list.append(current_cell)
                # closed_list.add(current_cell)

            """Check the neighbours of the cell"""
            self.check_neighbours(current_cell)
            """For each direction filter the valid moves"""
            directions = []
            # directions = list(filter(lambda x: self.board[self.neighbors[x][0]][self.neighbors[x][1]] != "#", self.neighbors))
            # directions = set()

            for direction in self.neighbors:
                
                """Check if the neighbour exists"""
                if self.neighbors[direction] is not None:
                    """If the neighbour is unvisited, append the direction to the list of possible directions"""
                    if self.board[self.neighbors[direction][0]][self.neighbors[direction][1]] != "#":
                        if self.neighbors[direction] != self.opening:
                            if self.neighbors[direction] not in closed_list:
                                directions.append(direction)
                                # directions.add(direction)
           
            """For each direction (successor)"""
            for direction in directions:
                """Calculate the g value"""
                g_temp = g[current_cell] + 1
                """Calculate the h value"""
                h_temp = self.heuristic(self.neighbors[direction], end)
                """Calculate the f value"""
                f_temp = g_temp + h_temp
                """if neighbour is in the open list with a better f value, skip it"""
                if self.neighbors[direction] in open_list:
                    if f_temp >= f[self.neighbors[direction]]:
                        continue
                """If the neighbour is in the closed list with a better f value, skip it"""
                if self.neighbors[direction] in closed_list:
                    if f_temp >= f[self.neighbors[direction]]:
                        continue
                """Append the current cell as the parent of the neighbour"""
                parent[self.neighbors[direction]] = current_cell
                """Update the g value"""
                g[self.neighbors[direction]] = g_temp
                """Update the f value"""
                f[self.neighbors[direction]] = f_temp
                """Remove the neighbour from the open list and the closed list"""
                if self.neighbors[direction] in open_list:
                    open_list.remove(self.neighbors[direction])
                # open_list.discard(self.neighbors[direction])
                if self.neighbors[direction] in closed_list:
                    closed_list.remove(self.neighbors[direction])
                # closed_list.discard(self.neighbors[direction])
                """Add the neighbour to the open list"""
                open_list.append(self.neighbors[direction])
                # open_list.add(self.neighbors[direction])

    """Draw the maze"""
    def draw_maze(self) -> None:
        self.board[self.entrance[0]][self.entrance[1]] = "S"
        self.board[self.exit[0]][self.exit[1]] = "E"
        for row in self.board:
            for cell in row:
                print(cell, end=" ")
            print()
        
    """Save the maze as a file.txt"""
    def save_maze(self, name:str):
        with open(f"mazes/{name}.txt", "w") as f:
            for lane in self.board:
                for cell in lane:
                    f.write(cell)
                f.write("\n")

    """Ascii to JPG"""
    def ascii_to_jpg(self, name:str):
        maze = self.board
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