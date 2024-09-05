class Animals:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("breathes")


class fish(
    Animals
):  # fish is base class and animal is parent class as base class inherits animals
    def __init__(self):
        super().__init__()  # this line is recommended but not strictly required for all the stuffs
        self.fins = 2

    def breathe(self):
        super().breathe()
        print("under water")


nemo = fish()
nemo.breathe()
print(nemo.num_of_eyes)
