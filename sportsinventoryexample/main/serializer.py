from rest_framework import serializers
from .models import SportsEquipments


class SportsEquipmentsSerializer(serializers.ModelSerializer):
    """
    serializer class used to python object into dict format
    """
    # name=serializers.CharField(max_length=50)
    # quntity = serializers.IntegerField()

    class Meta:
        model = SportsEquipments
        fields = ['name', 'quantity']
