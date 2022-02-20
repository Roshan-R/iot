from rest_framework import serializers
from .models import SensorType, Reading

class SensorTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model=SensorType
    
class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('__all__')

    def to_representation(self, instance):
        self.fields['user'] =  SensorTypeSerializer(read_only=True)
        return super(ReadingSerializer, self).to_representation(instance)