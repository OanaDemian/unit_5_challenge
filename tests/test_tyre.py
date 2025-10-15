from lib.tyre import *


"""
Given a tyre with a position 
when we add a new reading
we see the information reflected in get reading 
"""


def test_get_new_reading_when_one_tyre_added():
    tyre = Tyre("front-left")
    tyre.add_reading("34", "5", "2025/10/15")
    assert tyre.get_readings() == [{"pressure": "34", "tread depth": "5", "date": "2025/10/15"}]


"""
Given a tyre with a position 
when we add two new readings
we see the newer information reflected in get_latest_reading 
"""
def test_get_latest_reading_when_two_readings_added():
    tyre = Tyre("front-left")
    tyre.add_reading("34", "5", "2025/10/15")
    tyre.add_reading("30", "3", "2024/12/15")
    assert tyre.get_latest_reading() == {"pressure": "34", "tread depth": "5", "date": "2025/10/15"}