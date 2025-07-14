from rest_framework import serializers
from .models import *

class BMBCChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMBCChecksheet
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        fields = '__all__'

class BogieInspectionSerializer(serializers.ModelSerializer):
    bmbcChecksheet = BMBCChecksheetSerializer()
    bogieChecksheet = BogieChecksheetSerializer()
    bogieDetails = BogieDetailsSerializer()

    class Meta:
        model = BogieInspection
        fields = '__all__'

    def create(self, validated_data):
        bmbc_data = validated_data.pop('bmbcChecksheet')
        bogie_data = validated_data.pop('bogieChecksheet')
        details_data = validated_data.pop('bogieDetails')

        bmbc = BMBCChecksheet.objects.create(**bmbc_data)
        bogie = BogieChecksheet.objects.create(**bogie_data)
        details = BogieDetails.objects.create(**details_data)

        return BogieInspection.objects.create(
            bmbcChecksheet=bmbc,
            bogieChecksheet=bogie,
            bogieDetails=details,
            **validated_data
        )
    
    def update(self, instance, validated_data):
        bmbc_data = validated_data.pop('bmbcChecksheet', None)
        bogie_data = validated_data.pop('bogieChecksheet', None)
        details_data = validated_data.pop('bogieDetails', None)

        if bmbc_data:
            for attr, value in bmbc_data.items():
                setattr(instance.bmbcChecksheet, attr, value)
            instance.bmbcChecksheet.save()

        if bogie_data:
            for attr, value in bogie_data.items():
                setattr(instance.bogieChecksheet, attr, value)
            instance.bogieChecksheet.save()

        if details_data:
            for attr, value in details_data.items():
                setattr(instance.bogieDetails, attr, value)
            instance.bogieDetails.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
