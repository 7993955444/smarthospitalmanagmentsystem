from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    speciality = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class patient(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.CharField(max_length=100)
    patient = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    def __str__(self):
        return self.doctor

class Prescription(models.Model):
    patient = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    medicine = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.patient