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

    def get(self, request, id=None):
        # Don't really know why if condition exists
        if id:
            item = Reading.objects.get(id=id)
            serializer = ReadingSerializer(item)
            return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Reading.objects.all()
        serializer = ReadingSerializer(items, many=True)
        return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
