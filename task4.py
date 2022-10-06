import re


class Text:
    def __init__(self, text_file):
        self.text_file = text_file

    def Calculate_Chars(self):
        file = open(self.text_file, "r")
        chars = 0
        for i in file:
            chars += len(i)
            chars -= len(i.split()) - 1
        file.close()
        return chars


    def Calculate_Words(self):
        file = open(self.text_file, "r")
        words = sum(len(re.findall(r"[a-zA-Zа-яА-ЯёЁіІїЇ0-9]*[,.'-]?[a-zA-Zа-яА-ЯёЁіІєЄїЇ0-9]+", lines)) for lines in file)
        file.close()
        return words

    def Calculate_Senteces(self):
        file = open(self.text_file, "r")
        sentences = sum(len(re.findall(r"[A-ZА-ЯЁІЇ][^\.!?]*[\.!?]+", lines)) for lines in file)
        file.close()
        return sentences


text = Text("Test.txt")
print(text.Calculate_Chars())
print(text.Calculate_Words())
print(text.Calculate_Senteces())