from django.db import models
from django.utils.timezone import now


class SensorType(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    sensor_type = models.CharField(max_length=200)

    def __str__(self):
        return self.sensor_type 

class Reading(models.Model):
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    reading = models.FloatField()
    date = models.DateTimeField(default=now, blank=True)

    
    def __str__(self):
        return self.sensor_type.sensor_type + " : " + str(self.reading) 