import math
from typing import Any

import data


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# This function inputs its own and another time, then returns the total combined time.
# Input other as Time
# Output newTime as Time
# def time_add(self, other):
# return newTime
# Input(Time(10, 10,10), Time(20, 20, 20)
# Output(TIme(30, 30, 30)
def time_add(time1, time2):
    second = time1.second + time2.second
    minutes = time1.minute + time2.minute
    hours = time1.hour + time2.hour
    if (second >= 60):
        minutes += second // 60
        second = second % 60
    if (minutes >= 60):
        hours += minutes // 60
        minutes = minutes % 60

    newTime = data.Time(hours, minutes, second)
    return newTime

# Part 4
#This function inputs a lost of floats, then returns if the list is in decending order.
#Input list as a list of floats
#Output a boolean value
 #def is_decending(lista:list[float])-> bool:
    #return boolean
#Input([5.3, 3.8, 2.1, 1.2])
#Output(True)
def is_decending(lista:list[float])-> bool:
    for i in range(len(lista)-1):
        if(lista[i] < lista[i+1]):
            return False
    return True

# Part 5
#This function inputs a list of ints and a range of indexes, then returns the index of the largest value, return none when range is empty.
#Input list as a list of ints
#Input lower as an int
#Input upper as an int
#Output index as an int or none
 #def largest_between(list:list[int], lower:int, upper:int)->int:
    #return none
    #return index
#Input([1, 2, 3, 4, 5, 6], 2, 4)
#Output(5)
def largest_between(list:list[int], lower:int, upper:int)->int:
    if(lower > upper):
        return None
    highest = list[lower]
    index = 0
    for num in range(upper - lower+1):
        if(list[lower+num] > highest):
            highest = list[lower+num]
            index = lower+num

    return index


# Part 6
#This function inputs a list of points and returns the index of the point furthest form origin and none if list is empty.
#Input list as a list of Points
#Output furthest as an int or none
 #def furthest_from_origin(list:list[Point])-int:
    #return none
    #return furthest
#Input(Point(1,1), Point(2,2), Point(3,3))
#Output(2)
def furthest_from_origin(list)->int:
    if(len(list)==0):
        return None

    origin = data.Point(0,0)
    furthest = 0

    for num in range(len(list)):
        if(distance_from(origin, list[num]) > distance_from(origin, list[furthest])):
            furthest = num

    return furthest

#This function finds distance from two Points, taking two points and returning distance
#Input point1 as a Point
#Input point2 as a Point
#Output float
#def distance_from(point1:Point, point2:Point) -> float:
    #return float
def distance_from(point1, point2)-> float:
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)