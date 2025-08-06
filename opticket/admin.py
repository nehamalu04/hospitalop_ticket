from django.contrib import admin
from .models import Doctor, Description, OPPatient

admin.site.register(Doctor)
admin.site.register(Description)
admin.site.register(OPPatient)