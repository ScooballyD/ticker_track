import yfinance as yf
import tkinter as tk
from tkinter import Tk, BOTH
from tkinter.scrolledtext import ScrolledText
from banner import Window
from label import Block

#fb = yf.Ticker("META")


#price = fb.info["currentPrice"]
#close = fb.info["previousClose"]
#open = fb.info["previousClose"]
#dif = round(price - open, 2)
#ticker = fb.info["symbol"]
#name = fb.info["longName"]
#change  = f"{round(dif/open*100, 2)}%"

#print(ticker,":",open, ",", price, "=", change)
#print(name)
#for tick in tickers:
    #tag = yf.Ticker(tick)
    #open = tag.info["previousClose"]
    #price = tag.info["currentPrice"]
    #dif = round(price - open, 2)
    #print(tag.info["symbol"],":", price, ",", f"{round(dif/open*100, 2)}%")

#root = Tk()
#root.geometry("1920x20")
#root.attributes('-topmost', True)
#root.overrideredirect(True)



win = Window(1918, 20)


win.wait_for_close()
