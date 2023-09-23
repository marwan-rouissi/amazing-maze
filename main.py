from tkinter import *
import tkinter.messagebox
import tkinter.dialog
import tkinter.filedialog
import customtkinter
import tkinter.scrolledtext
from Class.maze import *
from Class.cell import *
from Class.solver import *

class App():

    def __init__(self):
        self.root = customtkinter.CTk()

        """Window settings"""
        self.appwidth = 650
        self.appheight = 400
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.x = (self.screenwidth / 2) - (self.appwidth / 2)
        self.y = (self.screenheight / 2) - (self.appheight / 2)
        self.root.geometry(f'{self.appwidth}x{self.appheight}+{int(self.x)}+{int(self.y)}')
        self.root.title("AmAzEinMaZe - Maze Generator & Solver")
        customtkinter.set_appearance_mode("dark")
        self.root.resizable(False, False)
        self.root.config(bg="#2A2A2A")

        """Labels"""
        title = customtkinter.CTkLabel(master=self.root, text="aMAZEing", font=customtkinter.CTkFont(family="Calibri", size=40, weight="bold"), fg_color="#2A2B2B")
        title.pack(anchor=tkinter.CENTER, pady=90)

        """Buttons"""
        generate_btn = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0, corner_radius=8, text="Generate Maze", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.generator_window)
        generate_btn.pack(anchor=tkinter.CENTER, pady=10)
        solve_btn = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0, corner_radius=8, text="Solve Maze", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.solver_window)
        solve_btn.pack(anchor=tkinter.CENTER, pady=10)
        """Vizualize button (uncomment to use))"""
        # vizualize_btn = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0, corner_radius=8, text="Vizualize Maze", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.vizualize_window)
        # vizualize_btn.pack(anchor=tkinter.CENTER, pady=10)

        self.root.mainloop()
    
    """Generation window"""
    def generator_window(self):
        self.gen_window = customtkinter.CTk()
        self.gen_window.geometry("600x550")
        self.gen_window._set_appearance_mode("dark")

        """Labels"""
        title = customtkinter.CTkLabel(master=self.gen_window, text="Maze Generator", font=customtkinter.CTkFont(family="Calibri", size=40, weight="bold"), fg_color="#2A2B2B")
        title.pack(anchor=tkinter.CENTER, pady=15)

        """Entry field for the parameters"""
        size_title = customtkinter.CTkLabel(master=self.gen_window, text="Maze size (int):", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), fg_color="#2A2B2B")
        size_title.pack(anchor=tkinter.CENTER, pady=10)
        self.size_entry = customtkinter.CTkEntry(master=self.gen_window, justify="center", textvariable=IntVar())
        self.size_entry.pack(anchor=tkinter.CENTER, pady=10)
        algorithm_title = customtkinter.CTkLabel(master=self.gen_window, text="Algorithm:", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), fg_color="#2A2B2B")
        algorithm_title.pack(anchor=tkinter.CENTER, pady=20)

        """Radio buttons"""
        self.varGenerator = IntVar()
        self.backtrack_radio = customtkinter.CTkRadioButton(master=self.gen_window, text="Backtracking", variable=self.varGenerator, value=1)
        self.backtrack_radio.pack(anchor=tkinter.CENTER, pady=5)
        self.kruskal_radio = customtkinter.CTkRadioButton(master=self.gen_window, text="Kruskal", variable=self.varGenerator, value=2)
        self.kruskal_radio.pack(anchor=tkinter.CENTER, pady=5)

        """Buttons"""
        apply_btn = customtkinter.CTkButton(master=self.gen_window, width=120, height=32, border_width=0, corner_radius=8, text="Apply", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.generator)
        apply_btn.pack(anchor=tkinter.CENTER, pady=50)

        self.gen_window.mainloop()
    
    """Solve window"""
    def solver_window(self):
        self.solv_window = customtkinter.CTk()
        self.solv_window.geometry("600x550")
        self.solv_window._set_appearance_mode("dark")

        """Labels"""
        title = customtkinter.CTkLabel(master=self.solv_window, text="Maze Solver", font=customtkinter.CTkFont(family="Calibri", size=40, weight="bold"), fg_color="#2A2B2B")
        title.pack(anchor=tkinter.CENTER, pady=15)

        """Entry field for the parameters"""
        maze_to_solve_title = customtkinter.CTkLabel(master=self.solv_window, text="Maze to solve:", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), fg_color="#2A2B2B")
        maze_to_solve_title.pack(anchor=tkinter.CENTER, pady=10)
        self.maze_to_solve_entry = customtkinter.CTkEntry(master=self.solv_window, justify="center", textvariable=IntVar())
        self.maze_to_solve_entry.pack(anchor=tkinter.CENTER, pady=10)
        algorithm_title = customtkinter.CTkLabel(master=self.solv_window, text="Algorithm:", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), fg_color="#2A2B2B")
        algorithm_title.pack(anchor=tkinter.CENTER, pady=20)

        """Radio buttons"""
        self.varSolver = IntVar()
        self.backtrack_radio = customtkinter.CTkRadioButton(master=self.solv_window, text="Backtracking", variable=self.varSolver, value=1)
        self.backtrack_radio.pack(anchor=tkinter.CENTER, pady=5)
        self.astar_radio = customtkinter.CTkRadioButton(master=self.solv_window, text="A Star", variable=self.varSolver, value=2)
        self.astar_radio.pack(anchor=tkinter.CENTER, pady=5)

        """Buttons"""
        apply_btn = customtkinter.CTkButton(master=self.solv_window, width=120, height=32, border_width=0, corner_radius=8, text="Apply", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.solver)
        apply_btn.pack(anchor=tkinter.CENTER, pady=50)

        self.solv_window.mainloop()
    
    """Save window"""
    def save_gen_window(self):
        self.gen_window.destroy()
        self.save_win = customtkinter.CTk()
        self.save_win.geometry("600x550")
        self.save_win._set_appearance_mode("dark")

        """Labels"""
        title = customtkinter.CTkLabel(master=self.save_win, text="Save Maze as:", font=customtkinter.CTkFont(family="Calibri", size=40, weight="bold"), fg_color="#2A2B2B")
        title.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        """Entry field for the parameters"""
        title = customtkinter.CTkLabel(master=self.save_win, text="Enter the maze's name to save:", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), fg_color="#2A2B2B")
        title.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.maze_to_save_entry = customtkinter.CTkEntry(master=self.save_win, placeholder_text="Maze name", justify="center")
        self.maze_to_save_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        """Buttons"""
        apply_btn = customtkinter.CTkButton(master=self.save_win, width=120, height=32, border_width=0, corner_radius=8, text="Apply", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.save_gen)
        apply_btn.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        self.save_win.mainloop()
    
    """Save solution window"""
    def save_solution_window(self):
        self.solv_window.destroy()
        self.save_solution_win = customtkinter.CTk()
        self.save_solution_win.geometry("600x550")
        self.save_solution_win._set_appearance_mode("dark")

        """Labels"""
        title = customtkinter.CTkLabel(master=self.save_solution_win, text="Save Solution as:", font=customtkinter.CTkFont(family="Calibri", size=40, weight="bold"), fg_color="#2A2B2B")
        title.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        """Entry field for the parameters"""
        title = customtkinter.CTkLabel(master=self.save_solution_win, text="Enter the maze's name to save:", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), fg_color="#2A2B2B")
        title.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.maze_to_save_entry = customtkinter.CTkEntry(master=self.save_solution_win, placeholder_text="Maze name", justify="center")
        self.maze_to_save_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        """Buttons"""
        apply_btn = customtkinter.CTkButton(master=self.save_solution_win, width=120, height=32, border_width=0, corner_radius=8, text="Apply", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.save_solution)
        apply_btn.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        self.save_solution_win.mainloop()
    
    """Vizualize window (uncomment to use)"""
    # """Vizualize window in the default image viewer"""
    # def vizualize_window(self):
    #     self.viz_window = customtkinter.CTk()
    #     self.viz_window.geometry("600x550")
    #     self.viz_window._set_appearance_mode("dark")

    #     """Labels"""
    #     title = customtkinter.CTkLabel(master=self.viz_window, text="Vizualize Maze", font=customtkinter.CTkFont(family="Calibri", size=40, weight="bold"), fg_color="#2A2B2B")
    #     title.pack(anchor=tkinter.CENTER, pady=15)

    #     """Entry field for the parameters"""
    #     maze_to_viz_title = customtkinter.CTkLabel(master=self.viz_window, text="Maze to vizualize:", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), fg_color="#2A2B2B")
    #     maze_to_viz_title.pack(anchor=tkinter.CENTER, pady=10)
    #     self.maze_to_viz_entry = customtkinter.CTkEntry(master=self.viz_window, justify="center", textvariable=IntVar())
    #     self.maze_to_viz_entry.pack(anchor=tkinter.CENTER, pady=10)

    #     """Buttons"""
    #     apply_btn = customtkinter.CTkButton(master=self.viz_window, width=120, height=32, border_width=0, corner_radius=8, text="Apply", fg_color="#18122B", hover_color="#443C68", font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"), command=self.vizualize)
    #     apply_btn.pack(anchor=tkinter.CENTER, pady=50)

    #     self.viz_window.mainloop()

    # """Vizualize the maze in the default image viewer"""
    # def vizualize(self):

    #     try:
    #         if self.maze_to_viz_entry.get() == "":
    #             tkinter.messagebox.showerror("Error", "Please enter a valid maze name to vizualize")
    #         name = str(self.maze_to_viz_entry.get())
    #         self.viz_window.destroy()
    #         # self.root.quit()
    #         self.open_maze(name)

    #     except FileNotFoundError:
    #         tkinter.messagebox.showerror("Error", "The maze does not exist")

    # """open a maze.jpg file in the default image viewer"""
    # def open_maze(self, name:str):
    #     img = Image.open(f"mazes/{name}.jpg")
    #     img.show()

    """Generator"""
    def generator(self):
        if self.size_entry.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a size")
        elif self.size_entry.get() == "0" or self.size_entry.get() == "1" or self.size_entry.get() == "2":
            tkinter.messagebox.showerror("Error", "The size must be greater than 2")
        else:
            size = int(self.size_entry.get())
            self.maze = Maze(size)
            if self.varGenerator.get() == 1:
                if size > 22:
                    tkinter.messagebox.showerror("Error", "The size of the maze must be less than 22")
                self.maze.recursive((0,0))
                self.maze.draw_maze()
                """ask if the user wants to save the maze as a file.txt"""
                save = tkinter.messagebox.askyesno("Save maze", "Do you want to save the maze as a file.txt?")
                if save:
                    self.save_gen_window()
            elif self.varGenerator.get() == 2:
                self.maze.kruskal()
                self.maze.draw_maze()
                save = tkinter.messagebox.askyesno("Save maze", "Do you want to save the maze as a file.txt?")
                if save:
                    self.save_gen_window()
            else:
                tkinter.messagebox.showerror("Error", "Please select an algorithm")

    """Load maze.txt file"""
    def load_maze(self, name:str) -> None:
        """Load the maze from a text file"""
        with open(f"mazes/{name}.txt", "r") as f:
            maze = f.readlines()
        """Remove the \n from the end of each line and convert the maze to a list of lists"""
        for i in range(len(maze)):
            maze[i] = maze[i].replace("\n", "")
            maze[i] = list(maze[i])
        return maze    
    
    """Solver"""
    def solver(self):
        if self.maze_to_solve_entry.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid maze name to solve")
        
        name = str(self.maze_to_solve_entry.get())
        self.solution = Solver(self.load_maze(name))
        size = len(self.load_maze(name))

        if self.varSolver.get() == 1:
            if size > 85:
                tkinter.messagebox.showerror("Error", "The size of the maze is too big for the recursive backtracking algorithm")
            else:
                self.solution.backtrack(self.solution.entrance)
                self.solution.draw_maze()
                tkinter.messagebox.showinfo("Maze solved", f"Maze {name}.txt solved with the recursive backtracking algorithm")
                """ask if the user wants to save the maze as a file.txt"""
                save = tkinter.messagebox.askyesno("Save maze", "Do you want to save the maze as a file.txt?")
                if save:
                    self.save_solution_window()
        elif self.varSolver.get() == 2:
            self.solution.AStar()
            self.solution.draw_maze()
            tkinter.messagebox.showinfo("Maze solved", f"Maze {name}.txt solved with the A* algorithm")
            """ask if the user wants to save the maze as a file.txt"""
            save = tkinter.messagebox.askyesno("Save maze", "Do you want to save the maze as a file.txt?")
            if save:
                self.save_solution_window()
        else:
            tkinter.messagebox.showerror("Error", "Please select an algorithm")

    """Save"""
    def save_gen(self):
        if self.maze_to_save_entry.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid maze name to save")
        name = str(self.maze_to_save_entry.get())
        self.maze.save_maze(name)
        self.maze.ascii_to_jpg(name)
        tkinter.messagebox.showinfo("Maze saved", f"Maze {name}.txt saved")
        self.save_win.destroy()
    
    """Save solution"""
    def save_solution(self):
        if self.maze_to_save_entry.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid maze name to save")
        name = str(self.maze_to_save_entry.get())
        self.solution.save_maze(name)
        self.solution.ascii_to_jpg(name)
        tkinter.messagebox.showinfo("Maze saved", f"Maze {name}.txt saved")
        self.save_solution_win.destroy()

if __name__ == "__main__":
    App()   