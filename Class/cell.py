class Cell:
    def __init__(self, x, y) -> None:
        self.pos = (x, y)
        self.walls = {"LEFT": True, "RIGHT": True, "UP": True, "DOWN": True}
        self.isvisited = False
        self.neighbors = {"LEFT": None, "RIGHT": None, "UP": None, "DOWN": None}
        self.next_cell = None
    
    def break_wall(self, direction:str, next_cell) -> None:
        opposition_pos = {"LEFT": "RIGHT", "RIGHT": "LEFT", "UP": "DOWN", "DOWN": "UP"}
        self.walls[direction] = False
        print(f"{self.pos} wall's after: {self.walls}")
        next_cell.walls[opposition_pos[direction]] = False
        
    """Check if all walls are broken"""
    def check_walls(self) -> None:
        if False in self.walls.values():
            return False
        else:
            return True