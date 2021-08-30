from django.db import models
from django.db.models.fields import CharField, DateField
from django.contrib.auth.models import User
import datetime
# Create your models here.

class ClientModelB(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    secondName = models.CharField(max_length=20, null=False)
    firstName = models.CharField(max_length=20, null=False)
    middleName = models.CharField(max_length=20, null=False)
    age = models.PositiveSmallIntegerField(null=False)
    address = models.CharField(max_length=150, null=False)
    mail = models.EmailField(null=False)
    imgBefore = models.ImageField(upload_to='images/', null=False)
    imgAfter = models.ImageField(upload_to='images/', null=False)
    comment1 = models.TextField(null=False)
    comment2 = models.TextField(null=False)
    comment3 = models.TextField(null=False)
    sel1 = models.CharField(max_length=100, null=False)
    sel2 = models.CharField(max_length=100, null=False)
    sel3 = models.CharField(max_length=100, null=False)
    date = models.DateField(default=datetime.date(1970, 10, 19))
    
    def __str__(self):
        return '{0} {1} {2}'.format(self.secondName, self.firstName, self.middleName)