import datetime

class Tyre():

    def __init__(self, position):
        self._position = position 
        self._readings = []
    
    def add_reading(self, pressure, tread_depth, date):
        # self.pressure = pressure
        # self.tread_depth = tread_depth
        # self.date = date 
        self._readings.append({"pressure": pressure, "tread depth": tread_depth, "date": date})

    def get_readings(self):
        return self._readings 
    
    def get_latest_reading(self):
        dates = []
        datetime_objects = []
        for reading in self._readings:
            dates.append(reading["date"])
        for date in dates:
            new_date = datetime.datetime.strptime(date, "%Y/%m/%d")
            datetime_objects.append(new_date)

        latest_date = max(datetime_objects)
        latest_date_string = datetime.datetime.strftime(latest_date, "%Y/%m/%d" )
        # latest_reading = [reading for reading, value in readings.items() if val == latest_date_string]

        for reading in self._readings:
            if reading["date"] == latest_date_string:
                return reading 
            
        
{'pressure': '34', 'tread depth': '5', 'date': '2025/10/15'}


# tyre = Tyre("front-left")
# tyre.add_reading("34", "5", "2025/10/15")
# tyre.add_reading("30", "3", "2024/12/15")
# print(tyre.get_latest_reading() )

        #retrieve the date key for every reading
        #sort the dates
        #retrieve the value for latest
        # now = datetime.datetime.now(pytz.utc)
        # youngest = max(dt for dt in datetimes if dt < now)
