from django.urls import path
from .views import *

urlpatterns = [
    path('/home', HomeAPIView.as_view(), name='home'),
    path('/about', AboutAPIView.as_view(), name='about'),
    path('/user', UserAPIView.as_view(), name='user'),
    path('/vd_lessons', Vd_lessonsAPIView.as_view(),name='vd_lessons'),
    path('/client', ClientAPIView.as_view(), name='client'),
    path('/team', TeamAPIView.as_view(), name='team'),
    path('/payment', PaymentAPIView.as_view(), name='payment'),
    path('web_sites', Web_sitesAPIView.as_view(), name='web_sites'),
    path('web_images', Web_imagesAPIView.as_view(), name='web_images'),
    path('')
]