from django.db import models

# Create your models here

class User(models.Model):
  first_name = models.CharField(max_length=60)
  last_name = models.CharField(max_length=60)
  
  birthday = models.DateField()
  gender = models.ChoiceField({"Male": "m", "Female": "f", "Unspecified": "u"})
  email = models.EmailField()
  password = models.CharField()
  username = models.CharField()
