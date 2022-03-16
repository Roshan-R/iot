from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .serializers import ReadingSerializer
from .models import Reading

class ReadingViews(APIView):
    def post(self, request):
        serializer = ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        height = Reading.objects.filter(sensor_type=1)
        water_level = Reading.objects.filter(sensor_type=2)
        
        height_serializer = ReadingSerializer(height, many=True)
        water_serializer = ReadingSerializer(water_level, many=True)

        return JsonResponse({"height": height_serializer.data,  "water_level": water_serializer.data}, status=status.HTTP_200_OK)
