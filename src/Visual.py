from lib.engine.Engine import Ray, Entity, EntitiesList, Game
from lib.math.Math import Matrix, Vector, Point
import tkinter as tk


class Canvas:
    def __init__(self, n: int, m: int, distances: Matrix):
        self.n = n
        self.m = m
        self.distances = distances

    def draw(canvaself):
        root = tk.Tk()
        root.geometry('800x600')
        canvas = Canvas(canvaself)
        canvas = tk.Canvas(root, width=600, height=400, bg='white')
        canvas.pack(anchor=tk.CENTER, expand=True)
        root.mainloop()

    def update(self, camera):
        pass


class Console(Canvas):
    def __init__(self):
        super(Console, self).__init__()

    def charmap(self, charmap: list[str]):
        self.charmap = charmap

