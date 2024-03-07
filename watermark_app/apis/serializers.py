from rest_framework import serializers
from ..models import Watermark


class WatermarkSerializer (serializers.ModelSerializer) :
    class Meta:
        model = Watermark
        fields = ("output",)

    def to_representation(self, instance:Watermark):
        data = {}
        if instance.output_path : 
            data['name'] = str(instance.original.name).split('/')[-1]
            data['url'] = instance.output_path
        return data

class CreateWatermarkSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Watermark
        fields = ('text','type','original','user')
    
    def validate(self, attrs):
        user = self.context['user']
        attrs['user'] = user
        return attrs
