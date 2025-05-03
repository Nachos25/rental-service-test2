from rest_framework import serializers
from .models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Apartment
        fields = [
            'id', 'name', 'slug', 'description', 'price', 
            'number_of_rooms', 'square', 'availability', 
            'owner', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']


class ApartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = [
            'name', 'description', 'price', 
            'number_of_rooms', 'square', 'availability'
        ]

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data) 