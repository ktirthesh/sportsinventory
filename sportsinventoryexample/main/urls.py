from django.urls import path

from .views import (EquipmentList,
                    AddEquipment,
                    NoQuantityEquipmentList,
                    UpdateEquipment)


urlpatterns = [
    path('equipments/all', EquipmentList.as_view(), name='equipments_all'),
    path('equipments/add', AddEquipment.as_view(), name='equipments_add'),
    path('equipments/no_quantity', NoQuantityEquipmentList.as_view(),
         name='equipments_no_quantity'),
    path('equipments/update', UpdateEquipment.as_view(), name='equipments_update'),
]
