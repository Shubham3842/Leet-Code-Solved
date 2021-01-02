class ParkingSystem(object):
    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small
​
        self.count_big = 0
        self.count_medium = 0
        self.count_small = 0
        
    def addCar(self, carType):
        if carType == 1 and self.big >= 1 and self.count_big < self.big:
            self.count_big += 1
            return True
        elif carType == 2 and self.medium >= 1 and self.count_medium < self.medium:
            self.count_medium += 1
            return True
        elif carType == 3 and self.small >= 1 and self.count_small < self.small:
            self.count_small += 1
            return True
        else:
            return False
            
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
