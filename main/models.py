from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MedicalRecord(models.Model):
    DEFAULT_MEDICAL_RECORD_TYPE = "Doctor's Visit"

    patient = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    date_of_visit = models.DateField()
    type_of_record = models.CharField(max_length=100, default=DEFAULT_MEDICAL_RECORD_TYPE)
    medical_notes = models.TextField()
    image = models.ImageField(upload_to='medical_images/')
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.patient.username} - {self.type_of_record}"
