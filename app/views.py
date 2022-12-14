from django.shortcuts import render

from .models import Pupil
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import PupilSerializers

class PupilViewset(ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializers
    
class PupilInfo(APIView):
    def get(self, request, one_id):
        data = Pupil.objects.filter(one_id=one_id)
        serializer = PupilSerializers(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def get(self, request):
        count = Pupil.objects.all().count()
        data = {
            'count':count
        }
        return Response(data=data, status=status.HTTP_202_OK)

