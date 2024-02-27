from django.urls import path

from .views import EquipmentList,AddEquipment



urlpatterns = [
    path('equipments/all', EquipmentList.as_view(), name='equipments_all'),
    path('equipments/add', AddEquipment.as_view(), name='equipments_add'),
    
]