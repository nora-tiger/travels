from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to="pics")
    des=models.TextField()

class Person(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="pics")
    des = models.TextField()



    def __str__(self):
        return self.name