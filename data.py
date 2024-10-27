import math
from typing import Any


# Representation of time as hours, minutes, and seconds
class Time:
    # Initialize a new Point object.
    # input: hour as an int
    # input: minute as an int
    # input: second as an int
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second


    #This function inputs its own and another time, then returns the total combined time.
    #Input other as Time
    #Output newTime as Time
    #def time_add(self, other):
        #return newTime
    #Input(Time(10, 10,10), Time(20, 20, 20)
    #Output(TIme(30, 30, 30)
    def time_add(self , other):

        second = self.second + other.second
        minutes = self.minute + other.minute
        hours = self.hour + other.hour
        if(second >= 60):
            minutes+= second//60
            second = second%60
        if(minutes >= 60):
            hours += minutes//60
            minutes = minutes%60

        newTime = Time(hours, minutes, second)
        return newTime

    # Provide a developer-friendly string representation of the object.
    # input: Time for which a string representation is desired. 
    # output: string representation


    # Compare the Time object with another value to determine equality.
    # input: Time against which to compare
    # input: Another value to compare to the Time
    # output: boolean indicating equality
    def __eq__(self, other:Any) -> bool:
        return (other is self or
                type(other) == Time and self.hour is other.hour and
                self.minute is other.minute and self.second is other.second)

    def __repr__(self) ->str:
        return "The time is Hour: {} Minute: {} Second: {}".format(str(self.hour), str(self.minute), str(self.second))



# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other:Any) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))




