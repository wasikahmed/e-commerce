from rest_framework import serializers

from .models import Customer, Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'phone', 'address', 'password', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')