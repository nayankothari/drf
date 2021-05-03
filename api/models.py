from django.db import models

# Create your models here.


class DataModel(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
