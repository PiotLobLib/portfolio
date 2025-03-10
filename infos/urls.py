from django.urls import path
from infos import views


urlpatterns = [
    path('', views.home, name='home'),
    path('me/', views.me, name='me'),
    path('contact/', views.contact, name='contact'),
]
