from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    IIN = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    planned_start_time = models.CharField(max_length=50, blank=True, null=True)
    planned_finish_time = models.CharField(max_length=50, blank=True, null=True)
    company_branch = models.CharField(max_length=100, blank=True, null=True)
    real_start_time = models.CharField(max_length=50, blank=True, null=True)
    real_finish_time = models.CharField(max_length=50, blank=True, null=True)
    document_date = models.DateField(blank=True, null=True)