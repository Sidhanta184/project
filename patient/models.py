from django.db import models
from django.utils import timezone
from doctor.models import Doctor
from medical.models import Medicine,Medical
from lab.models import Lab,Test
# Create your models here.
gender = (('male','Male'),('female','Female'),('other','Other'))
class Patient(models.Model):
    id=models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=gender)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100,blank=True,null=True)




    def __str__(self):
        return self.name

class DoctorComment(models.Model):
    comment = models.TextField()
    patient = models.OneToOneField(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class MedicineSuggest(models.Model):
    medicine_name = models.ForeignKey(Medicine)
    buy_date = models.DateField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    suggest_by = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    sell_by = models.ForeignKey(Medical,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return self.medicine_name

class TestSuggest(models.Model):
    test = models.ForeignKey(Lab)
    test_date = models.DateField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    suggest_by = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    test_by = models.ForeignKey(Medical,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return self.test
