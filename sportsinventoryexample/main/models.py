from django.db import models

# Create your models here.

class SportsEquipments(models.Model):
    """
    fields 
        -- name is unique reason for update and create  
        -- quantity for value number of items present in inventory 
    """
    name =models.CharField(max_length=50,unique=True) 
    quantity=models.IntegerField(default=0) 

    class Meta:
        db_table="sports_equipments"