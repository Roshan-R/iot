from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .serializers import ReadingSerializer, InputSerializer
from .models import Reading, SensorType

class ReadingViews(APIView):
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            saveSensorInputData(serializer.data)
            return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        height = Reading.objects.filter(sensor_type=1)
        water_level = Reading.objects.filter(sensor_type=2)
        
        height_serializer = ReadingSerializer(height, many=True)
        water_serializer = ReadingSerializer(water_level, many=True)

        return JsonResponse({"height": height_serializer.data,  "water_level": water_serializer.data}, status=status.HTTP_200_OK)

mapping = {
    "height" : 1,
    "water_level" : 2,
    "dew" : 3, 
    "precipitation" : 4,
    "humidity" : 5,
    "density" : 6,
    "speed" : 7,
    "direction" : 8,
    "temperature" : 9,
}

def saveSensorInputData(data):
    for sensor in data:
        if sensor != 'time':
            sensortype = SensorType.objects.all()[mapping[sensor] - 1]
    temperature = Reading(sensor_type=sensortype, reading=data['temperature'], date=data['time'])
    temperature.save()
    print(temperature)

