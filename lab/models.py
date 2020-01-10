from django.db import models
from MyUser.models import MyUser
# Create your models here.
class Lab(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Test(models.Model):
    test_name = models.CharField(max_length=100)
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.test_name
