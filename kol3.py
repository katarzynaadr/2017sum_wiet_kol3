#source_chooco

import unittest

from planePosition import PlanePosition


class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.plane_position = PlanePosition()

    def test_tilt_correction_positive(self):
        self.plane_position.current_position = 0
        self.plane_position.tilt_correction(0.3)
        self.assertEqual(0.3, self.plane_position.current_position)

    def test_tilt_correction_negative(self):
        self.plane_position.current_position = 0
        self.plane_position.tilt_correction(-0.3)
        self.assertEqual(-0.3, self.plane_position.current_position)

    def test_tilt_correction_zero(self):
        self.plane_position.current_position = 0
        self.plane_position.tilt_correction(0)
        self.assertEqual(0, self.plane_position.current_position)

    def test_correction_flight_positon_equals_max_correction(self):
        self.plane_position.current_position = 0.3
        self.plane_position.correction_flight()
        self.assertEqual(0, self.plane_position.current_position)

    def test_correction_flight_current_greater_than_max(self):
        self.plane_position.current_position = 0.5
        self.plane_position.correction_flight()
        self.assertEqual(0.2, self.plane_position.current_position)

    def test_correction_flight_current_less_than_max(self):
        self.plane_position.current_position = 0.2
        self.plane_position.correction_flight()
        self.assertEqual(0.5, self.plane_position.current_position)
        
    def test_show_current_position_integer(self):
        self.plane_position.current_position = 10
        self.plane_position.show_current_position()
        self.assertEqual('Current position: 10', self.plane_position.current_position_string)
        
    def test_show_current_position_float(self):
        self.plane_position.current_position = 0.1
        self.plane_position.show_current_position()
        self.assertEqual('Current position: 0.1', self.plane_position.current_position_string)


if __name__ == "__main__":
    unittest.main()

