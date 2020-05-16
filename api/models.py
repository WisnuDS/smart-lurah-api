from django.db import models
from django_mysql.models import EnumField


# Create your models here.


class User(models.Model):
    telegram_id = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    status = EnumField(choices=["verified","unverified","rejected"],default="unverified")
    url_ktp_photo = models.CharField(max_length=300, default="url")
    url_self_photo = models.CharField(max_length=300, default="url")

    def __str__(self):
        return self.name


class ServiceRequirements(models.Model):
    name_requirement = models.CharField(max_length=100)

    def __str__(self):
        return self.name_requirement


class Services(models.Model):
    type_service = models.CharField(max_length=100)
    status = EnumField(choices=["active","inactive"],default="active")

    def __str__(self):
        return self.type_service


class DetailRequirements(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    requirement = models.ForeignKey(ServiceRequirements, on_delete=models.CASCADE)

    def __str__(self):
        return self.service


class Arrangement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    status = EnumField(choices=["verified","not verified","rejected","finished"],default="not verified")

    def __str__(self):
        return self.user, self.service, self.status, self.date


class FileRequirement(models.Model):
    arrangement = models.ForeignKey(Arrangement, on_delete=models.CASCADE)
    requirement = models.ForeignKey(ServiceRequirements, on_delete=models.CASCADE)
    url_file = models.CharField(max_length=300, default="url")

    def __str__(self):
        return self.arrangement_id, self.requirement_id, self.url_file
