# Car Readings Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Car                        │
│                            │
│ - tyre_positions  = []              │
│ - add_tyre_info(tyre)      │
│ - history()                │
│   => {tyre_position: [readings]}           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────────────┐
│ Tyre(position)                 │
│                                 │
│ - position                      │
│ - pressure                      │
  - tread_depth 
  - add_reading() =>  position: {pressure:  33, tread_depth: 4.5, date_taken: 2025/10/09}                 │
│ - readings:[{date_taken: {pressure:  34, tread_depth: 4.5}}, {date_taken: {pressure:  30, tread_depth: 4.6}}]                   │
│             │
└─────────────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car:
    # User-facing properties:
    #  self._tyres a dictionary of instances of Track

    def __init__(self):
        # self._tyres = {"front left": {"pressure": 34, "treads_depth": 1.6mm, "date_taken": "2025/10/15"}, "front right": {}, "rear left" : {}, "rear right": {}}


    def add_tyre_info(self, tyre):
        # Parameters:
        #   tyre: an instance of Tyre
        # Side-effects:
        #   Adds the tyre info to the tyres property of the self object acording to the tyre position e.g. self.tyres[tyre.position]["pressure"] = tyre.pressure
        pass # No code here yet

    def history(self):
        # Parameters:
        # None
        # Returns:
        #   A list of the Tyre objects that have readings
        pass # No code here yet

    def car_details(self):
        # Parameters:
        # None
        # Returns:
        # A formated string including the tyres' positions, latest readings and when those were => # "The latest reading for front left tyre was on 2025/09/25. The pressure was 33 PSI and the tread_depth was 4.5mm"

class Tyre:
    # User-facing properties:
    #   _position: string

    def __init__(self, position):
        # Parameters:
          #   self._position: string
          #   self.readings = [] 
        # Side-effects:
        #   Sets the tyre object properties
        pass # No code here yet

    def add_reading(self, pressure, tread_depth, date):
        # Returns:
        #   None
        # Side-effects: Adds the reading to the readings property of the self object readings =[{"pressure": 34, "treads_depth": 1.6mm, "date_taken": "2025/10/15"}]
        pass # No code here yet

    def get_readings(self):
        # Parameters:
        # None
        # Returns:
        #  a list of all the reading for that tyre object
        # Side-effects:
        # None

    def get_latest_reading(self):
    # Parameters:
    # None
    # Returns:
    #  a dictionary object with all the reading info for the latest reading
    # Side-effects:
    # None

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a car
When we add a tyre
We see the latest reading for that tyre
"""
car = Car()
tyre_front_left = Tyre("front left")
tyre_front_left.add_reading("34", "5", "2025/08/30")
car.add_tyre_info(tyre_front_left)
car.car_details() # => "The latest reading for front left tyre was on 2025/08/30. The pressure was 34 PSI and the tread_depth was 5mm"
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a tyre with a position 
when we add a new reading
we see the information reflected in get reading 
"""
tyre = Tyre("front-left")
tyre.add_reading("34", "5", "2025/10/15")
tyre.get_readings => [{"pressure": "34", "treads_depth": "5", "date_taken": "2025/10/15"}]

"""
Given a tyre with a position 
when we add two new readings
we see the newer information reflected in get_latest_reading 
"""
tyre = Tyre("front-left")
tyre.add_reading("34", "5", "2025/10/15")
tyre.add_reading("30", "3", "2024/12/15")
tyre.get_latest_reading => [{"pressure": "34", "treads_depth": "5", "date_taken": "2025/10/15"}]

"""
Given a tyre with a position 
when we add multiple new readings
we see the newer information reflected in get_latest_reading 
"""
tyre = Tyre("front-left")
tyre.add_reading("34", "5", "2025/10/15")
tyre.add_reading("30", "3", "2024/12/15")
tyre.add_reading("31", "2", "2023/10/15")
tyre.add_reading("28", "3", "2022/12/15")

tyre.get_latest_reading => [{"pressure": "34", "treads_depth": "5", "date_taken": "2025/10/15"}]

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
