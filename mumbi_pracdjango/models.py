from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(unique=True, blank=False, max_length=40)
    destination = models.CharField(blank=False, max_length=100)
    period = models.CharField(blank=False, max_length=50)
    nationality = models.CharField(blank=False, max_length=30)
    people = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name
