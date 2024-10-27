import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    #### add_Time Tests
    def test_add_Time_1(self):
        time1 = data.Time(1, 2, 3)
        time2 = data.Time(1, 2, 3)
        time3 = lab5.time_add(time1, time2)
        self.assertEqual("The time is Hour: 2 Minute: 4 Second: 6", repr(time3))

    def test_add_Time_2(self):
        time1 = data.Time(2, 65, 65)
        time2 = data.Time(2, 65, 65)
        time3 = lab5.time_add(time1, time2)
        self.assertEqual("The time is Hour: 6 Minute: 12 Second: 10", repr(time3))

    # Part 4
    def test_is_decending_1(self):
        lista = [1.1, 2.1, 3.1, 4.1, 5.1]
        self.assertEqual(False, lab5.is_decending(lista))

    def test_is_decending_2(self):
        lista = [5.1, 4.1, 3.1, 2.1, 1.1]
        self.assertEqual(True, lab5.is_decending(lista))

    # Part 5
    def test_largest_between_1(self):
        lista = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(lab5.largest_between(lista, 2, 5), 5)

    def test_largest_between_2(self):
        lista = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(lab5.largest_between(lista, 3, 1), None)

    # Part 6
    def test_furthest_1(self):
        point1 = data.Point(2, 2)
        point2 = data.Point(3, 3)
        point3 = data.Point(4, 4)
        list = [point1, point2, point3]
        self.assertEqual(lab5.furthest_from_origin(list), 2)

    def test_furthest_2(self):
        list = []
        self.assertEqual(lab5.furthest_from_origin(list), None)



if __name__ == '__main__':
    unittest.main()
