from .serializers import ReadingSerializer, InputSerializer
from .models import Reading, SensorType

def createJson():
        height = Reading.objects.filter(sensor_type=1)
        dew = Reading.objects.filter(sensor_type=3)
        precipitation = Reading.objects.filter(sensor_type=4)
        humidity = Reading.objects.filter(sensor_type=5)
        density = Reading.objects.filter(sensor_type=6)
        speed = Reading.objects.filter(sensor_type=7)
        direction = Reading.objects.filter(sensor_type=8)
        temperature = Reading.objects.filter(sensor_type=9)
        pressure = Reading.objects.filter(sensor_type=10)

        height_serializer = ReadingSerializer(height, many=True)
        dew_serializer = ReadingSerializer(dew, many=True)
        precipitation_serializer = ReadingSerializer(precipitation, many=True)
        humidity_serializer = ReadingSerializer(humidity, many=True)
        density_serializer = ReadingSerializer(density, many=True)
        speed_serializer = ReadingSerializer(speed, many=True)
        direction_serializer = ReadingSerializer(direction, many=True)
        temperature_serializer = ReadingSerializer(temperature, many=True)
        pressure_serializer = ReadingSerializer(pressure, many=True)

        return {
            "height" : height_serializer.data,
            "dew_point" : dew_serializer.data,
            "rain_gauge" : precipitation_serializer.data,
            "relative_humidity" : humidity_serializer.data,
            "air_density" : density_serializer.data,
            "wind_speed" : speed_serializer.data,
            "wind_direction" : direction_serializer.data,
            "ambient_temperature" : temperature_serializer.data,
            "athmospheric_pressure" : pressure_serializer.data
        }

