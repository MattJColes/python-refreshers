class Car():
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage
		
	def move(self):
		print(f"{self.color} car with {self.mileage} kms of distance travelled") 


# Inheriting from parent class
class Mustang(Car):
    # Method overriding
    def move(self):
        print(f"{self.color} mustang with {self.mileage} kms of distance travelled")

car_1 = Car("blue", 20_000)
car_2 = Mustang("red", 30_000)

car_2.move()
