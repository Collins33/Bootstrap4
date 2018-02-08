from django.test import TestCase
from .models import Category
# Create your tests here.

#class to test category model
class categoryTest(TestCase):
    #set up method to be run before each test
    def setUp(self):
        self.category=Category(category_name="chocolate")

    #tear down runs after every test
    def tearDown(self):
        Category.objects.all().delete()    

    #test that it is an instance of Category model
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    #test the method to save a category to the database
    def test_save_adds_to_database(self):
        self.category.saveCategory()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)    
            
