from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'not specified'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name 

class Address(models.Model):
    ownder = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    