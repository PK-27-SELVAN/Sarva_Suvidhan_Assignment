from rest_framework import serializers
from .models import *

class WheelFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelFields
        fields = '__all__'

class WheelInspectionSerializer(serializers.ModelSerializer):
    fields = WheelFieldsSerializer()

    class Meta:
        model = WheelInspection
        fields = '__all__'

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        fields = WheelFields.objects.create(**fields_data)
        return WheelInspection.objects.create(fields=fields, **validated_data)

    def update(self, instance, validated_data):
        fields_data = validated_data.pop('fields', None)

        if fields_data:
            wheel_fields_instance = instance.fields
            for attr, value in fields_data.items():
                setattr(wheel_fields_instance, attr, value)
            wheel_fields_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
