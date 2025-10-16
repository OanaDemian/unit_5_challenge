from lib.tyre import Tyre
from lib.car import Car 


"""
Initially we have no readings for any tyre
"""
def test_no_readings_for_tyres():
    car = Car()
    # front_left = Tyre("front left")
    assert car.tyres["front left"].get_readings() == []
    


"""
Given a car
When we add a tyre
We see the reading for that tyre
"""

def test_when_we_add_a_tyre_gets_the_reading():
    car = Car()
    tyre_front_left = Tyre("front left")
    tyre_front_left.add_reading("34", "5", "2025/08/30")
    car.add_tyre_info(tyre_front_left)
    assert car.tyres["front left"].get_readings()[0] == {'pressure': '34', 'tread depth': '5', 'date': '2025/08/30'}
    