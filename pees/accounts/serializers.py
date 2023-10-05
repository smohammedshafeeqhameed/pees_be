# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'age', 'gender', 'phone']
        extra_kwargs = {
            'password': {'write_only': True},
            'age': {'required': False, 'allow_null': True},
            'gender': {'required': False, 'allow_null': True},
            'phone': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data.get('age'),
            gender=validated_data.get('gender'),
            phone=validated_data.get('phone')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user