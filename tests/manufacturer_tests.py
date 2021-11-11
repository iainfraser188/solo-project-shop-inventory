import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer_1 = Manufacturer("Taylor",1974,"EL Cajon")
        self.manufacturer_2 = Manufacturer("Gibson",1902, "Michigan")


    def test_manufacturer_has_name(self):
        self.assertEqual("Taylor",self.manufacturer_1.company_name)

    def test_manufacturer_has_founded_date(self):
        self.assertEqual(1974,self.manufacturer_1.founded)    

    def test_manufacturer_has_location(self):
        self.assertEqual("Michigan",self.manufacturer_2.location)    