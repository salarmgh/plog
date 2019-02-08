from rest_framework import serializers
from authz.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'created_at')
        extra_kwargs = {'password': {'required': False}}

    def to_representation(self, obj):
        data = super(UserSerializer, self).to_representation(obj)
        data.pop("password")
        return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        instance = User.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email) 
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.save()
        return instance

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {'username': {'validators': []}}
