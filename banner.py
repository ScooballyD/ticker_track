import tkinter as tk
from tkinter import Tk, BOTH, Canvas
from label import Block, tickers

class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title("")
        #self.__root.call('wm', 'attributes', '.', '-topmost', True)
        self.__root.overrideredirect(True)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.blocks = []

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        for block in self.blocks:
            block.update()

    def wait_for_close(self):
        self.create_blocks()
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed.")

    def create_blocks(self):
        offset = 1900
        for tick in tickers:
            self.blocks.append(Block(self.__root, tick, offset))
            offset = offset + 200

    def close(self):
        self.test.run = False
        self.__running = False

