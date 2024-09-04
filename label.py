import tkinter as tk
import yfinance as yf
import time

tickers = ["AMZN", "GOOGL", "META", "MSFT", "NVDA",]


class Block:
    def __init__(self, root, tick, offset):
        tag = yf.Ticker(tick)
        self.open = tag.info["previousClose"]
        self.price = tag.info["currentPrice"]
        self.dif = round(self.price - self.open, 2)


        self.label = tk.Label(root, text=f"{tick}: {self.price}, {round(self.dif/self.open*100, 2)}%", bg="black", fg="white")
        self.x = offset
        self.run = True
        self.label.place(x= self.x, y=0)

    def update(self):
        self.x = self.x - 1
        if self.x < -100:
            self.x = 1900
        self.label.place(x= self.x, y=0)
        time.sleep(.01)


