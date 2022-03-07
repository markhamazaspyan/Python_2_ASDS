from abc import ABC, abstractmethod

class InstrumentCollection(ABC):
    @abstractmethod

    def make(self):
        pass


class Pen(InstrumentCollection):
    def __init__(self, act):
        self.act = act
        self.name = "Pen"

    def make(self):
        print(f"Instrument's job is: {self.act}")


class Pencil(InstrumentCollection):
    def __init__(self, act):
        self.act = act
        self.name = "Pencil"

    def make(self):
        print(f"Instrument's job is: {self.act}")


class Rubber(InstrumentCollection):
    def __init__(self, act):
        self.act = act
        self.name = "Rubber"

    def make(self):
        print(f"Instrument's job is: {self.act}")


class Box(InstrumentCollection):
    def __init__(self):
        self.instruments = []

    def add(self, instrument):
        self.instruments.append(instrument)

    def remove(self, instrument):
        print(f"Deleting {instrument.name}")
        self.instruments.remove(instrument)

    def make(self):
        for instruments in self.instruments:
            instruments.make()

    def get_children(self, idx):
        return self.instruments[idx].name


if __name__ == "__main__":

    pen = Pen("black drawer")

    pencil = Pencil("pink drawer")

    rubber = Rubber("all color clearer")

    top_box = Box()

    top_box.add(pen)

    top_box.add(pencil)

    top_box.add(rubber)

    top_box.make()

    print(f"The first element is {top_box.get_children(1)}")

    top_box.remove(pen)

    print(f"Now the first element is {top_box.get_children(1)}")