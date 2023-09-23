from Class.maze import *
from Class.cell import *

"""Test the maze generators"""

"""Generate a maze with the recursive backtracking algorithm and save it"""
def backtrack_generation() -> None:
    n = input("Enter the size of the maze: ")
    maze = Maze(int(n))
    maze.recursive((0,0))
    print()
    print("Maze generated with the recursive backtracking algorithm:")
    print()
    maze.print_maze()
    maze.draw_maze()
    name = input("Enter the name of the maze: ")
    maze.save_maze(name)
    maze.ascii_to_jpg(name)

"""Generate a maze with the kruskal algorithm and save it"""
def kruskal_generation() -> None:
    n = input("Enter the size of the maze: ")
    maze = Maze(int(n))
    maze.kruskal()
    print()
    print("Maze generated with the kruskal algorithm:")
    print()
    maze.print_maze()
    maze.draw_maze()
    name = input("Enter the name of the maze: ")
    maze.save_maze(name)
    maze.ascii_to_jpg(name)

	
if __name__ == "__main__":

    """max size of the maze is 22x22.
    Over 22x22: RecursionError: maximum recursion depth exceeded in comparison"""
    # backtrack_generation()
    kruskal_generation()
