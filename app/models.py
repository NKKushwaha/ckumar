from django.db import models

# Create your models here.

class DetailInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
class Contactform(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    company = models.CharField(max_length=100)
    url = models.URLField()
    service = models.CharField( max_length=100)
    budget = models.CharField( max_length=100)
    goal = models.TextField()

    def __str__ (self):
        return self.first_name