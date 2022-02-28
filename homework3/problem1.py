"""
Use adapter pattern and classes of your choice. Create a structure where you have 1-2 adaptees
that have a method that returns some text in spanish. Have an adapter which will have a method that
translates the text to english. Have examples of the usage of your class structure.
"""


class Adaptee1:
    def __init__(self):
        self.spanish_text = "Ola"

class Adaptee2:
    def __init__(self):
        self.spanish_text = "Como estas"


class Adapter:

    def trainslate_spanish_to_english(self):
        if self.text=="Ola":
            self.translation = "Hello"
        elif self.text=="Como estas":
            self.translation = "How are you"
        else:
            raise Exception("Not smart enough")



class Translator(Adapter):
    def __init__(self, adaptee):
        self.text = adaptee.spanish_text

    def translate(self):
        self.trainslate_spanish_to_english()
        print(self.translation)


if __name__=="__main__":
    text = Adaptee1()
    t = Translator(text)
    t.translate()

    text1 = Adaptee2()
    t1 = Translator(text1)
    t1.translate()

