from django.db import models
from patient.models import Patient
from doctor.models import Doctor,Departments


# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.CharField(max_length=3)
    patient_email=models.EmailField(max_length=50)
    patient_gender= models.CharField(max_length=7)
    phone_number = models.CharField(default=0, max_length=15)
    department_name = models.ForeignKey(Departments, on_delete=models.CASCADE,related_name="department_names",verbose_name="Department Name")
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name="doctor_name",verbose_name="Doctor Name")
    appoinment_date = models.DateField(verbose_name='Appoinment Date', null=True)
    serial_number = models.IntegerField(verbose_name='Serial Number')
    user_id = models.IntegerField(verbose_name='User_id')
    is_cancelled = models.BooleanField(default=False)

    
    class Meta:
        db_table = "appoinment"
        
    def __str__(self):
        return str(self.appoinment_date)
    


