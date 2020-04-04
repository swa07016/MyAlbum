from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    writer = models.CharField(max_length=255)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title