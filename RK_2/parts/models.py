from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=256, verbose_name="Manufacturer name")

    def __str__ (self):
        return self.name

class Part (models.Model):
    name = models.CharField(max_length=256, verbose_name="Part name")
    cost = models.PositiveIntegerField(verbose_name="Part cost")
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None,
        related_name="parts"
    )

    def __str__(self):
        return self.name