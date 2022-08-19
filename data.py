import pandas
import random

# -----------------------------DATA-------------------------------#

data = pandas.read_csv("data/english_words.csv")


class Data():

    def __init__(self):
        self.data_dict = data.to_dict(orient="records")

    def english_word(self):
        self.english_number = random.randint(0, len(self.data_dict) - 1)
        self.english_random = self.data_dict[self.english_number]["English"]
        return self.english_random

    def polish_word(self):
        self.polish_random = self.data_dict[self.english_number]["Polish"]
        return self.polish_random

