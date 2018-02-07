from django.db import models

# Create your models here.


#category model
class Category(models.Model):
    category_name=models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

#ingredient model
class Ingredient(models.Model):
    ingredient=models.CharField(max_length=30)

    def __str__(self):
        return self.ingredient        


#confectionery model
class Confectionery(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(blank=True)
    created=models.DateField(auto_now_add=True)
    first_image=models.ImageField(upload_to='product/',blank=True)
    second_image=models.ImageField(upload_to='product/',blank=True)
    third_image=models.ImageField(upload_to='product/',blank=True)
    fourth_image=models.ImageField(upload_to='product/',blank=True)
    #relationships
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name=None)#one to many relationship
    ingredients=models.ManyToManyField(Ingredient,related_name=None)

    def __str__(self):
        return self.name









    
