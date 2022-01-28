import unittest
from src.steeringwheel_scrapper.scrapper import Scrapper


class TestScrapper(unittest.TestCase):
    def test_class_return_valid_status_code(self):
        scrapper = Scrapper('http://google.com')
        self.assertEqual(scrapper._getstatuscode(), 200)
