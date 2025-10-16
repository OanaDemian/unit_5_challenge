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

"""
Given a car
When we add two different tyres
With two different readings
We can see the readings for each of them individually 
"""

def test_when_we_add_two_tyres_gets_the_reading_for_each():
    car = Car()
    tyre_front_left = Tyre("front left")
    tyre_front_left.add_reading("34", "5", "2025/08/30")
    tyre_front_left.add_reading("29", "4", "2024/07/10")
    tyre_front_right = Tyre("front right")
    tyre_front_right.add_reading("30", "4", "2025/10/13")
    tyre_front_right.add_reading("32", "2", "2021/07/05")
    car.add_tyre_info(tyre_front_left)
    car.add_tyre_info(tyre_front_right)
    assert car.tyres["front left"].get_readings() == [{'pressure': '34', 'tread depth': '5', 'date': '2025/08/30'}, {'pressure': '29', 'tread depth': '4', 'date': '2024/07/10'}]
    assert car.tyres["front right"].get_readings() == [{'pressure': '30', 'tread depth': '4', 'date': '2025/10/13'}, {'pressure': '32', 'tread depth': '2', 'date': '2021/07/05'}]
"""
Given a car
When we add one tyre 
With three different readings
We can get the latest reading for that tyre
"""
def test_when_we_add_one_tyre_3_readings_gets_latest_reading():
    car = Car()
    tyre_front_left = Tyre("front left")
    tyre_front_left.add_reading("30", "4", "2025/10/13")
    tyre_front_left.add_reading("32", "2", "2021/07/05")
    tyre_front_left.add_reading("29", "4", "2024/07/10")
    car.add_tyre_info(tyre_front_left)
    assert car.tyres["front left"].get_latest_reading() == {'pressure': '30', 'tread depth': '4', 'date': '2025/10/13'}
    
    # [{'pressure': '30', 'tread depth': '4', 'date': '2025/10/13'}, {'pressure': '32', 'tread depth': '2', 'date': '2021/07/05'}, {'pressure': '29', 'tread depth': '4', 'date': '2024/07/10'}]

"""
Given a car
With 4 tyres
With different readings
We can get a nicely formatted message with the latest reading for all 4 tyres.
"""

def test_get_latest_reading():
    car = Car()
    tyre_front_left = Tyre("front left")
    tyre_front_right = Tyre("front right")
    tyre_rear_left = Tyre("rear left")
    tyre_rear_right = Tyre("rear right")
    tyre_front_left.add_reading("30", "4", "2025/10/13")
    tyre_front_right.add_reading("32", "2", "2021/07/05")
    tyre_front_left.add_reading("30", "4", "2020/10/13")
    tyre_front_right.add_reading("32", "2", "2019/07/05")
    tyre_rear_left.add_reading("29", "4", "2024/07/10")
    tyre_rear_right.add_reading("35", "3", "2023/01/02")
    car.add_tyre_info(tyre_front_left)
    car.add_tyre_info(tyre_front_right)
    car.add_tyre_info(tyre_rear_left)
    car.add_tyre_info(tyre_rear_right)
    assert car.latest_car_details() == 'Front left: On the 2025/10/13 the pressure was 30 PSI and the tread depth was 4mm. Front right: On the 2021/07/05 the pressure was 32 PSI and the tread depth was 2mm. Rear left: On the 2024/07/10 the pressure was 29 PSI and the tread depth was 4mm. Rear right: On the 2023/01/02 the pressure was 35 PSI and the tread depth was 3mm.'
    