from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .serializers import ReadingSerializer, InputSerializer
from .models import Reading, SensorType
from .util import createJson

# mapping = {
    # "height" : 1,
    # "water_level" : 2,
    # "dew" : 3,
    # "precipitation" : 4,
    # "humidity" : 5,
    # "density" : 6,
    # "speed" : 7,
    # "direction" : 8,
    # "temperature" : 9,
    # "pressure" : 10,
# }

class ReadingViews(APIView):
    # on post request 
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            saveSensorInputData(serializer.data)
            return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    # on get request
    def get(self, request):
        return JsonResponse(createJson(), status=status.HTTP_200_OK)


def saveSensorInputData(data):
    for sensor in data:
        if sensor != 'time':
            sensortype = SensorType.objects.all()[mapping[sensor] - 1]
            reading = Reading(sensor_type=sensortype, reading=data[str(sensortype)], date=data['time'])
            reading.save()
