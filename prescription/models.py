from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    form = models.CharField(max_length=100, blank=True, null=True)
    mg = models.CharField(max_length=50, blank=True, null=True)
    default_dosage = models.CharField(max_length=100, blank=True, null=True)
    instruction = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.mg if self.mg else ''}"


class Prescription(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_age = models.IntegerField(default=0)
    patient_gender = models.CharField(max_length=20, default='نارینه')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"نسخه: {self.patient_name} - {self.created_at.strftime('%Y-%m-%d')}"


class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, related_name='items', on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=200)
    mg = models.CharField(max_length=50, blank=True, null=True)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instruction = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.medicine_name} - {self.dosage}"