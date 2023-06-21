# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


# @api_view(['GET', 'POST'])
# def smart_home(request):
#     if request.method == 'GET':
#         sensor = Sensor.objects.all()
#         data = SensorSerializer(sensor, many=True)
#         return Response(data.data)
#     if request.method == 'POST':
#         return Response({'Status': 'Ok'})


# class SmartHomeView(APIView):
#     def get(self, request):
#         sensor = Sensor.objects.all()
#         data = SensorSerializer(sensor, many=True)
#         return Response(data.data)
#
#     def post(self, request):
#         return Response({'Status': 'Ok'})

class SensorsView(ListCreateAPIView):
    '''получение датчиков'''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(RetrieveUpdateAPIView):
    '''получение информации по датчику'''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(CreateAPIView):
    """Добавить температуру"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
