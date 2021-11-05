import unittest
from models.guitar import Guitar

class TestGuitar(unittest.TestCase):
    def setUp(self):
        self.guitar_1 = Guitar("Les Paul","Sun Burst","Gibson","Electric",6,1998,300,500)
        self.guitar_2 = Guitar("Stratocaster","Black","fender","Electric",6,2010,250,350)
        self.guitar_3 = Guitar("Big Baby", "Mahogany","Taylor","Acoustic",6,1960,200,350)
        self.guitar_4 = Guitar("Academy","Rosewood","Taylor","Acoustic",12,1979,400,550)



    def test_guitar_has_name(self):
        self.assertEqual("Les Paul",self.guitar_1.guitar_name)    

    def test_guitar_has_colour(self):
        self.assertEqual("Black",self.guitar_2.colour)

    def test_guitar_has_maker(self):
        self.assertEqual("Taylor",self.guitar_4.manufacturer)    

    def tests_guitar_has_type(self):
        self.assertEqual("Electric",self.guitar_2.type)

    def tests_guitar_has_no_of_strings(self):
        self.assertEqual(6,self.guitar_2.no_of_strings)

    def tests_guitar_has_no_of_strings_12string(self):
        self.assertEqual(12,self.guitar_4.no_of_strings) 

    def tests_guitar_has_made_date(self):
        self.assertEqual(1960,self.guitar_3.production_date)

    def tests_guitar_has_stock_price(self):
        self.assertEqual(200,self.guitar_3.stock_price) 

    def test_guitar_has_retail_price(self):
        self.assertEqual(500,self.guitar_1.selling_price)                 

