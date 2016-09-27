from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Metric(models.Model):
  users = models.ManyToManyField(User, through = 'Vote')
  name = models.CharField(max_length = 255)

class Vote(models.Model):
  metric = models.ForeignKey(Metric, on_delete = models.CASCADE)
  user = models.ForeignKey(Person, on_delete = models.CASCADE)
  rating = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
  email = models.EmailField

  def __str__(self):
    return str(self.rating)
