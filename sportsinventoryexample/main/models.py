from django.db import models

# Create your models here.

class SportsEquipments(models.Model):
    name =models.CharField(max_length=50)
    quantity=models.IntegerField(default=0)

    class Meta:
        db_table="sports_equipments"