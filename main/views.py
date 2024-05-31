from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authtoken.admin import User

from .models import (Users,
                     Vd_lessons,
                     Client,
                     Payment,
                     About,
                     Team,
                     Web_sites,
                     Web_images)
from .serializers import (UserSerializer,
                          Vd_lessonsSerializer,
                          ClientSerializer,
                          PaymentSerializer,
                          AboutSerializer,
                          TeamSerializer,
                          Web_sitesSerializer,
                          Web_imagesSerializer)
# Create your views here.
class UserAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class Vd_lessonsAPIView(generics.ListAPIView):
    queryset = Vd_lessons.objects.all()
    serializer_class = Vd_lessonsSerializer

class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class PaymentAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class Web_sitesAPIView(generics.ListAPIView):
    queryset = Web_sites.objects.all()
    serializer_class = Web_sitesSerializer

class Web_imagesAPIView(generics.ListAPIView):
    queryset = Web_images.objects.all()
    serializer_class = Web_imagesSerializer

class HomeAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer