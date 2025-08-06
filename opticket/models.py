from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Description(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OPPatient(models.Model):
    op_no = models.IntegerField(unique=True)
    op_date = models.DateField()
    patient_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    token_no = models.CharField(max_length=20, blank=True)
    appointment_details = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    # description = models.ForeignKey(Description, on_delete=models.SET_NULL, null=True)
    description = models.ManyToManyField(Description)
    qty = models.IntegerField(default=1)
    rate = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    payment_mode = models.CharField(max_length=50)
    received_amount = models.FloatField(default=0)
    balance_amount = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total_amount = models.FloatField(default=0)

    def __str__(self):
        return f"OP {self.op_no} - {self.name}"
        # return f"{self.op_no} - {self.name}"

