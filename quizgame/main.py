class Car:
    def __init__(self, modelname, modelnumber, numberofseats):
        self.model_name = modelname
        self.model_number = modelnumber
        self.numberofseats = numberofseats
        self.numberoftires = 4
        self.follower = 0
        self.following = 0

    def follow(self, car):
        car.follower += 1
        self.following += 1


car1 = Car("maruti gusuki", "42069", "5")
car2 = Car("XUV700", "0001", "7")

print(car1.model_name)
print(car2.numberofseats)
print(car1.numberoftires)

car1.follow(car2)

print(car2.follower)
print(car2.following)

print(car1.follower)
print(car1.following)
