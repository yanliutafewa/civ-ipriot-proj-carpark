import unittest
from src.parse_config import ConfigParser


class TestConfigParser(unittest.TestCase):

    def test_get_Config_data(self):

        config_info = {'CarParksCenter': [{'name': 'Moondalup CarPark Management Center'}]}

        parser = ConfigParser('../src/config.json')
        data = parser.get_config_data()

        self.assertEqual(config_info, data)

    def test_get_car_parks_center_name(self):

        center_name = 'Moondalup CarPark Management Center'

        parser = ConfigParser('../src/config.json')
        parser.get_car_parks_center_name()

        self.assertEqual(center_name, parser.get_car_parks_center_name())
