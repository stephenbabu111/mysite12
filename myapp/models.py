from django.db import models


# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.name
class exam_halls(models.Model):
    roomno=models.CharField(max_length=5)
    rows=models.PositiveSmallIntegerField(default=1)
    columns=models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.roomno
