from django.db import models
from MyUser.models import MyUser
# Create your models here.
class Medical(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(verbose_name="Price per unit")
    expiry_date = models.DateField()
    company = models.CharField(blank=True,null=True,max_length=100)
    medical = models.ForeignKey(Medical,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name
