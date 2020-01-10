from django.contrib import admin
from .models import Patient,MedicineSuggest,TestSuggest,DoctorComment
# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicineSuggest)
admin.site.register(TestSuggest)
admin.site.register(DoctorComment)
