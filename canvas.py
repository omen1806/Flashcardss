from tkinter import *
from data import Data
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "white"


class MainWindow():

    def __init__(self, main):
        self.canvas = Canvas(main, width=880, height=586, highlightthickness=0, bg= BACKGROUND_COLOR)
        self.canvas.grid(column=0, row=0, columnspan=2)

        # ------------------ CANVAS IMAGES --------------------------------------------

        self.image_back = PhotoImage(file="images/card_back.png")
        self.image_front = PhotoImage(file="images/card_front.png")

        # ------------------ CANVAS FIRTS IMAGE ----------------------------------------

        self.image_on_canvas = self.canvas.create_image(440,300, image = self.image_front)

        # ------------------ CANVAS TEXTS -----------------------------------------------

        self.upper_text_canvas = self.canvas.create_text(440, 200, text="English", fill=BACKGROUND_COLOR,
                                               font=("arial", 40, "italic"))
        self.lower_text_canvas = self.canvas.create_text(440, 330, text=Data().english_word(), fill=BACKGROUND_COLOR,
                                               font=("arial", 50, "bold"))

        # -------------------- BUTTONS ----------------------------

        self.right_button = Button(main, command=self.english_card)
        self.right_button_img = PhotoImage(file="images/right.png")
        self.right_button.config(image=self.right_button_img, pady=20)
        self.right_button.grid(column=0, row=1)

        self.wrong_button = Button(main, command=self.english_card)
        self.wrong_button_img = PhotoImage(file="images/wrong.png")
        self.wrong_button.config(image=self.wrong_button_img, pady=20)
        self.wrong_button.grid(column=1, row=1)

        self.canvas.after(3000, self.polish_card)

        # --------------------- FUNCTIONS ----------------------------

    def english_card(self):
        self.canvas.itemconfig(self.image_on_canvas, image = self.image_front)
        self.canvas.itemconfig(self.upper_text_canvas, text= "English", fill=BACKGROUND_COLOR)
        self.canvas.itemconfig(self.lower_text_canvas, text= Data().english_word(), fill=BACKGROUND_COLOR)


    def polish_card(self):
        self.canvas.itemconfig(self.image_on_canvas, image = self.image_front)
        self.canvas.itemconfig(self.upper_text_canvas, text= "Polski", fill=WHITE)
        self.canvas.itemconfig(self.lower_text_canvas, text= Data().polish_word(), fill=WHITE)


