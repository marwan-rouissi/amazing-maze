from Class.solver import *

"""Test the maze solvers"""

"""Load the maze from a text file"""
def load_maze(name:str) -> None:
    """Load the maze from a text file"""
    with open(f"mazes/{name}.txt", "r") as f:
        maze = f.readlines()
    """Remove the \n from the end of each line and convert the maze to a list of lists"""
    for i in range(len(maze)):
        maze[i] = maze[i].replace("\n", "")
        maze[i] = list(maze[i])
    return maze

"""Recursive backtracking algorithm"""
def backtrack() -> None:
    maze_name = input("Enter the name of the maze to solve: ")
    """Solve the maze with the recursive backtracking algorithm"""
    solver = Solver(load_maze(maze_name))
    solver.draw_maze()
    solver.backtrack(solver.entrance)
    solver.draw_maze()
    print()
    print("The maze has been solved with the recursive backtracking algorithm.")
    print()
    solved_maze_name = input("Enter the name of the solved maze: ")
    solver.save_maze(solved_maze_name)
    solver.ascii_to_jpg(solved_maze_name)

"""A* algorithm"""
def AStar() -> None:
    # maze_name = "100k"
    maze_name = input("Enter the name of the maze to solve: ")
    """Solve the maze with the A* algorithm"""
    solver = Solver(load_maze(maze_name))
    solver.AStar()
    solver.draw_maze()
    print()
    print("The maze has been solved with the A* algorithm.")
    print()
    solved_maze_name = input("Enter the name of the solved maze: ")
    solver.save_maze(solved_maze_name)
    solver.ascii_to_jpg(solved_maze_name)

if __name__ == "__main__":
    # backtrack()
    AStar()