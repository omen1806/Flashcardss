from tkinter import *
import pandas
import random
from canvas import MainWindow
BACKGROUND_COLOR = "#B1DDC6"
# -----------------------------DATA-------------------------------#

# -----------------------------UI-------------------------------- #

window = Tk()
window.config(width=900, height=900, background=BACKGROUND_COLOR)
window.title("FlashCard")

MainWindow(window)

window.mainloop()




