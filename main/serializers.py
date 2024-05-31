from rest_framework import serializers
from .models import (Users,
                     Vd_lessons,
                     Client,
                     Payment,
                     About,
                     Team,
                     Web_sites,
                     Web_images)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class Vd_lessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vd_lessons
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

class Web_sitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web_sites
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

class Web_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web_images
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
