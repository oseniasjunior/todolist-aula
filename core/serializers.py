from rest_framework import serializers
from core import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'

    def validate(self, data):
        if data['estimated_hours'] > 10:
            raise serializers.ValidationError('Estimated hours cannot be greater than 10')
        return super().validate(data)


    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['custom_filed'] = 'Campo customizado para teste'
        return response