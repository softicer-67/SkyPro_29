from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class WrongEmail:
    def call(self, value):
        if value.split('@')[1] == "rambler.ru":
            raise serializers.ValidationError("Нельзя регистрироваться с почтой rambler")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # fields = 'username', 'password'

    def create(self, validated_data):
        email = serializers.EmailField(validators=[WrongEmail()])
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


# class EmailSerializer(serializers.ModelSerializer):
#     email = models.EmailField(max_length=100,
#                               validators=[DomainValidator('rambler.ru')], unique=True, null=True, blank=True)
#
#     class Meta:
#         model = User
#         fields = 'email'
#         fields = 'username', 'password'
#
#     def create(self, validated_data):
#         return EmailSerializer(**validated_data)


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
        # fields = 'name', 'price', 'description', 'is_published'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
