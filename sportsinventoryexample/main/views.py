from django.shortcuts import render
import re
from rest_framework import generics, status
from rest_framework.response import Response

from .models import SportsEquipments
from .serializer import SportsEquipmentsSerializer

# Create your views here.


class EquipmentList(generics.GenericAPIView):

    queryset = SportsEquipments.objects.all()
    http_method_names = ['post']

    def post(self, request):
        queryset = self.get_queryset()
        serializer = SportsEquipmentsSerializer(queryset, many=True)
        return Response(serializer.data)


# Create your views here.
class AddEquipment(generics.GenericAPIView):

    http_method_names = ['post']
    validation_dict = {
        "name": {'required': True, "regex_": "^[a-zA-Z0-9]+$"},
        "quantity": {'required': False, "regex_": "^[0-9]+$"}
    }

    def post(self, request):
        try:
            request_data = request.POST.copy() or request.data.copy()
            error_data = {}
            for key, value in self.validation_dict.items():
                if value["required"] and not request_data.get(key, None):
                    error_data[key] = "{} is mandetory.".format(key)
                if request_data.get(key,False) and value.get('regex_') and not re.match(value['regex_'], str(request_data.get(key))):
                    error_data[key] = "{} in invalid format".format(key)

            if error_data:
                return Response({"status": False, "data": error_data}, status=status.HTTP_400_BAD_REQUEST)
            speqpts = SportsEquipments.objects.filter(
                name=request_data.get('name'))

            if speqpts.exists():
                return Response({"status": False, "data": "record already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer_object = SportsEquipmentsSerializer(data=request_data)

            if serializer_object.is_valid():
                serializer_object.save()
            else:
                return Response({"status": False, "data": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": True, "data": "record saved successfully"})
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"status": False, "data": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
