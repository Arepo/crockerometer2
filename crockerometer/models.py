from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Metric(models.Model):
  users = models.ManyToManyField(User, through = 'Rating')
  name = models.CharField(max_length = 255)
  def __str__(self):
    return self.name

class Rating(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  metric = models.ForeignKey(Metric, on_delete = models.CASCADE)
  average_score = models.DecimalField(decimal_places=10, default=None, blank=True, max_digits=11, null=True)
  def __str__(self):
    rating = "{:.1f}".format(self.average_score) if self.average_score else "No votes"
    return str(self.user) + ' for ' + str(self.metric) + ': ' + rating

class Vote(models.Model):
  rating = models.ForeignKey(Rating, on_delete = models.CASCADE)
  score = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
  email = models.EmailField()
  def __str__(self):
    return str(self.score)


  # Some practice drivel
  def decorator_func(func):
    func.attribute = 'foo'

  @decorator_func
  def random_func(self):
    pass

