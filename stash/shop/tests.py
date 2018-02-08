from django.test import TestCase
from .models import Category
# Create your tests here.

#class to test category model
class categoryTest(TestCase):
    #set up method to be run before each test
    def setUp(self):
        self.category=Category(category_name="chocolate")

    #test that it is an instance of Category model
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
            
