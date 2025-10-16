from tyre import Tyre

class Car():

    def __init__(self):
        self.tyres ={
        "front left":   {Tyre("front left")},
        "front right":  {Tyre("front right")}, 
        "rear left" :   {Tyre("rear left")}, 
        "rear right":   {Tyre("rear right")}
        }

    def add_tyre_info():
        pass

    def latest_car_details():
        pass


car = Car()
print(car.tyres)