from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы


# class SensorSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=256)
#     description = serializers.CharField(max_length=256)


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
