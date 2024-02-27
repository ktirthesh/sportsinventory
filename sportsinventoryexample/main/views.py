import re
from rest_framework import generics, status
from rest_framework.response import Response
from .models import SportsEquipments
from .serializer import SportsEquipmentsSerializer
from .utils import validation_dict

# Create your views here.


class EquipmentList(generics.GenericAPIView):
    queryset = SportsEquipments.objects.all()
    http_method_names = ['post']

    def post(self, request):
        """
        list all items
        """
        queryset = self.get_queryset()
        serializer = SportsEquipmentsSerializer(queryset, many=True)
        return Response(serializer.data)


class NoQuantityEquipmentList(generics.GenericAPIView):

    queryset = SportsEquipments.objects.filter(quantity=0)
    http_method_names = ['post']

    def post(self, request):
        """ 
        Get Items which have no quantity left
        """
        queryset = self.get_queryset()
        serializer = SportsEquipmentsSerializer(queryset, many=True)
        return Response(serializer.data)


# Create your views here.
class AddEquipment(generics.GenericAPIView):

    http_method_names = ['post']

    def post(self, request):
        """
        Create Item entry
        """
        try:
            request_data = request.POST.copy() or request.data.copy()
            error_data = {}
            for key, value in validation_dict.items():
                if value["required"] and not request_data.get(key, None):
                    error_data[key] = "{} is mandetory.".format(key)
                if request_data.get(key, False) and value.get('regex_') and not re.match(value['regex_'], str(request_data.get(key))):
                    error_data[key] = "{} in invalid format".format(key)

            if error_data:
                return Response({"status": False, "data": error_data}, status=status.HTTP_400_BAD_REQUEST)
            sports_equipments_object = SportsEquipments.objects.filter(
                name=request_data.get('name'))

            if sports_equipments_object.exists():
                return Response({"status": False, "data": "record already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer_object = SportsEquipmentsSerializer(data=request_data)

            if serializer_object.is_valid():
                serializer_object.save()
            else:
                return Response({"status": False, "data": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": True, "data": "record saved successfully"})
        except Exception:
            return Response({"status": False, "data": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# Get Items which have no quantity left


class UpdateEquipment(generics.GenericAPIView):

    http_method_names = ['post']

    def post(self, request):
        """
        Update Item entry
        """
        try:
            request_data = request.POST.copy() or request.data.copy()
            error_data = {}
            for key, value in validation_dict.items():
                if value["required"] and not request_data.get(key, None):
                    error_data[key] = "{} is mandetory.".format(key)
                if request_data.get(key, False) and value.get('regex_') and not re.match(value['regex_'], str(request_data.get(key))):
                    error_data[key] = "{} in invalid format".format(key)

            if error_data:
                return Response({"status": False, "data": error_data}, status=status.HTTP_400_BAD_REQUEST)
            sports_equipments_object = SportsEquipments.objects.filter(
                name=request_data.get('name'))

            if sports_equipments_object.exists():
                serializer_object = SportsEquipmentsSerializer(
                    sports_equipments_object[0], data=request.data, partial=True)
                if serializer_object.is_valid():
                    serializer_object.save()
                else:
                    return Response({"status": False, "data": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status": False, "data": "No record found"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"status": True, "data": "record updated successfully"})
        except Exception:
            return Response({"status": False, "data": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
