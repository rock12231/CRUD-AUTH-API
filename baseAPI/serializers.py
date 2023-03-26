from rest_framework import serializers
from baseAPI.models import DesignModel
from django.contrib.auth.models import User


# Design Serializer
class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignModel
        fields = '__all__'
    # Override create methods
    def create(self, validated_data):
        return super().create(validated_data)
    # Override update methods
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
    # Override create methods
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user