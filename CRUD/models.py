from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    familymembers = models.IntegerField()


    def __str__(self) -> str:
        return self.name