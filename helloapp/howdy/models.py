from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here

class Course(models.Model):
    code = models.CharField(max_length = 6, default = '')
    name = models.CharField(max_length = 200, default = '')
    prereq = models.CharField(max_length = 200, default = '')
    credithours = models.IntegerField(validators = [MaxValueValidator(4), MinValueValidator(1)], default = 0)
    fall = models.BooleanField(default = True)
    spring = models.BooleanField(default = True)
    #__str__ displays course codes when .all() is called
    def __str__(self):
        return self.code
