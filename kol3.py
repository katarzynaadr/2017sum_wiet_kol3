#source_chooco

import unittest

from planePosition import PlanePosition


class PlanPositionTest(unittest.TestCase):
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

    def test_show_current_position_string(self):
        self.plane_position.current_position = '10'
        self.plane_position.show_current_position()
        self.assertEqual('Current position: 10', self.plane_position.current_position_string)

    def test_init_with_defaults(self):
        self.assertEqual(0, self.plane_position.current_position)
        self.assertEqual(0.3, self.plane_position.max_correction)

    def test_init_with_floats(self):
        self.plane_position = PlanePosition(0.5, 0.5)
        self.assertEqual(0.5, self.plane_position.current_position)
        self.assertEqual(0.5, self.plane_position.max_correction)

    def test_init_with_valid_str(self):
        self.plane_position = PlanePosition('0.5', '0.5')
        self.assertEqual(0.5, self.plane_position.current_position)
        self.assertEqual(0.5, self.plane_position.max_correction)

    def test_init_with_invalid_str(self):
        with self.assertRaises(ValueError):
            self.plane_position = PlanePosition('asd', '0.5')

    def test_init_with_ints(self):
        self.plane_position = PlanePosition(1, 1)
        self.assertEqual(1., self.plane_position.current_position)
        self.assertEqual(1., self.plane_position.max_correction)


if __name__ == "__main__":
    unittest.main()

