from django.db import models
from MyUser.models import MyUser

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.department_name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    join_date = models.DateField(null=True,blank=True)
    age = models.IntegerField(blank=True,null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    def get_join_date(self):
        return self.join_date
