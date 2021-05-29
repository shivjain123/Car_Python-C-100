class Car(object):
    def __init__(self, color, height, brandName, carName, speed):
        self.color = color
        self.height = height
        self.brandName = brandName
        self.carName = carName
        self.speed = speed
    
    def start(self):
        print("The Car has Started.")
    
    def stop(self):
        print("The Car has Stopped.")
    
    def accelerate(self):
        print("The Car has Accelerated.")
    
    def brake(self):
        print("The Car has Slowed down.")

    def changeGear(self):
        print("The Car's Gear has been changed.")

audi = Car("Blue", 6, "Audi", "Audi007", 60)
print()
audi.start()
print()
print(audi.color)
print()
wolkswagen = Car("Golden", 4, "Wolkswagen", "Wolkswagen002", 70)
wolkswagen.stop()
print()