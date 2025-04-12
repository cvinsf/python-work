class Aircraft:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def fly_up(self, ):
        self.height += self.speed

class Helicopter(Aircraft):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self):
        self.direction += 90
    
    def mystats(self):
        return [self.speed, self.height]

mychopper = Helicopter(100, 50)
print(mychopper.mystats())