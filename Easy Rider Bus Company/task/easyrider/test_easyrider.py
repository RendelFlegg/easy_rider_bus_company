import unittest
import easyrider


class TestEasyrider(unittest.TestCase):
    def test_check_bus_id(self):
        self.assertTrue(easyrider.check_bus_id(16), 'Error when checking 16')
        self.assertFalse(easyrider.check_bus_id('16'), 'Error when checking "16"')
        self.assertFalse(easyrider.check_bus_id(''), 'Error when checking empty string')

    def test_stop_bus_id(self):
        self.assertTrue(easyrider.check_stop_id(16), 'Error when checking 16')
        self.assertFalse(easyrider.check_stop_id('16'), 'Error when checking "16"')
        self.assertFalse(easyrider.check_stop_id(''), 'Error when checking empty string')

    def test_stop_name(self):
        self.assertTrue(easyrider.check_stop_name('Sesame Street'), 'Error when checking "Sesame Street"')
        self.assertTrue(easyrider.check_stop_name('London Boulevard'), 'Error when checking "London Boulevard"')
        self.assertTrue(easyrider.check_stop_name('Upper Sesame Street'), 'Error when checking "Sesame street"')
        self.assertFalse(easyrider.check_stop_name('SesameStreet'), 'Error when checking "SesameStreet"')
        self.assertFalse(easyrider.check_stop_name('sesame Street'), 'Error when checking "sesame Street"')
        self.assertFalse(easyrider.check_stop_name('Sesame street'), 'Error when checking "Sesame street"')
        self.assertFalse(easyrider.check_stop_name('Sesame Sesame'), 'Error when checking "Sesame Sesame"')
        self.assertFalse(easyrider.check_stop_name('Street'), 'Error when checking "Street"')
        self.assertFalse(easyrider.check_stop_name(''), 'Error when checking empty string')
        self.assertFalse(easyrider.check_stop_name(9), 'Error when checking 9')

    def test_next_stop(self):
        self.assertTrue(easyrider.check_bus_id(16), 'Error when checking 16')
        self.assertFalse(easyrider.check_bus_id('16'), 'Error when checking "16"')
        self.assertFalse(easyrider.check_bus_id(''), 'Error when checking empty string')

    def test_stop_type(self):
        self.assertTrue(easyrider.check_stop_type('S'), 'Error when checking "S"')
        self.assertTrue(easyrider.check_stop_type('O'), 'Error when checking "O"')
        self.assertTrue(easyrider.check_stop_type('F'), 'Error when checking "F"')
        self.assertFalse(easyrider.check_stop_type(''), 'Error when checking empty string')
        self.assertFalse(easyrider.check_stop_type('X'), 'Error when checking "X"')
        self.assertFalse(easyrider.check_stop_type('SOF'), 'Error when checking "SOF"')
        self.assertFalse(easyrider.check_stop_type(16), 'Error when checking 16')
        self.assertFalse(easyrider.check_stop_type('16'), 'Error when checking "16"')

    def test_a_time(self):
        self.assertTrue(easyrider.check_a_time('08:19'), 'Error when checking "08:19"')
        self.assertTrue(easyrider.check_a_time('23:15'), 'Error when checking "23:15"')
        self.assertFalse(easyrider.check_a_time('28:19'), 'Error when checking "28:19"')
        self.assertFalse(easyrider.check_a_time('08:75'), 'Error when checking "08:75"')
        self.assertFalse(easyrider.check_a_time('8:19'), 'Error when checking "8:19"')
        self.assertFalse(easyrider.check_a_time('08:1'), 'Error when checking "08:1"')
        self.assertFalse(easyrider.check_a_time('08.19'), 'Error when checking "08.19"')
        self.assertFalse(easyrider.check_a_time(''), 'Error when checking ""')
        self.assertFalse(easyrider.check_a_time(08.12), 'Error when checking 08.12')


if __name__ == '__main__':
    unittest.main()
