from lib.tyre import Tyre
from lib.car import Car 


"""
Initially we have no readings for any tyre
"""
def test_no_readings_for_tyres():
    car = Car()
    # front_left = Tyre("front left")
    assert car.tyres["front left"].get_readings == []
    


"""
Given a car
When we add a tyre
We see the latest reading for that tyre
"""
# => "The latest reading for front left tyre was on 2025/08/30. The pressure was 34 PSI and the tread_depth was 5mm"

# def test_when_we_add_a_tyre_get_latest_reading():
#     car = Car()
#     tyre_front_left = Tyre("front left")
#     tyre_front_left.add_reading("34", "5", "2025/08/30")
#     car.add_tyre_info(tyre_front_left)
#     car.history()
#     pass