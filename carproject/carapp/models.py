from django.db import models
app_name = 'carapp'

# Create your models here.
class Car(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name