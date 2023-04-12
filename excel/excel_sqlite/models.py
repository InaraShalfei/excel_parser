from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    IIN = models.IntegerField()
    company = models.CharField(max_length=100)
    planned_start_time = models.CharField(max_length=50)
    planned_finish_time = models.CharField(max_length=50)
    company_branch = models.CharField(max_length=100)
    real_start_time = models.CharField(max_length=50)
    real_finish_time = models.CharField(max_length=50)
    document_date = models.DateField()